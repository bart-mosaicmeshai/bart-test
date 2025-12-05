"""
LM Studio API client for OLMo 3 experiments.
Handles inference requests and response analysis.
"""

import json
import time
from datetime import datetime
from typing import Optional, Dict, Any
import requests


class OLMoClient:
    """Client for interacting with OLMo 3 via LM Studio's local API."""

    def __init__(self, base_url: str = "http://localhost:1234/v1", model: str = "allenai/olmo-3-32b-think"):
        self.base_url = base_url
        self.model = model
        self.session = requests.Session()

    def verify_connection(self) -> bool:
        """Verify LM Studio API is accessible and model is loaded."""
        try:
            response = self.session.get(f"{self.base_url}/models")
            response.raise_for_status()
            models = response.json()

            loaded_models = [m["id"] for m in models.get("data", [])]
            if self.model in loaded_models:
                print(f"✓ Connected to LM Studio API")
                print(f"✓ Model loaded: {self.model}")
                return True
            else:
                print(f"✗ Model '{self.model}' not found in loaded models")
                print(f"  Available models: {', '.join(loaded_models)}")
                return False
        except Exception as e:
            print(f"✗ Connection failed: {e}")
            return False

    def complete(
        self,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 8192,
        stream: bool = False,
        **kwargs
    ) -> Dict[str, Any]:
        """
        Send completion request to LM Studio API.

        Returns dict with:
        - response: The model's text response
        - thinking: Extracted thinking traces (if present)
        - tokens_prompt: Tokens in the prompt
        - tokens_completion: Tokens in the completion
        - total_tokens: Total tokens used
        - duration_seconds: Time taken for generation
        """
        start_time = time.time()

        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "stream": stream,
            **kwargs
        }

        try:
            response = self.session.post(
                f"{self.base_url}/chat/completions",
                json=payload,
                timeout=600  # 10 minute timeout for long responses
            )
            response.raise_for_status()
            result = response.json()

            duration = time.time() - start_time

            # Extract response text
            response_text = result["choices"][0]["message"]["content"]

            # Parse thinking traces if present (OLMo 3 Think uses <think>...</think> tags)
            thinking, answer = self._extract_thinking(response_text)

            # Extract token usage
            usage = result.get("usage", {})

            return {
                "response": response_text,
                "thinking": thinking,
                "answer": answer,
                "tokens_prompt": usage.get("prompt_tokens", 0),
                "tokens_completion": usage.get("completion_tokens", 0),
                "total_tokens": usage.get("total_tokens", 0),
                "duration_seconds": duration,
                "raw_result": result
            }

        except Exception as e:
            return {
                "error": str(e),
                "duration_seconds": time.time() - start_time
            }

    def _extract_thinking(self, text: str) -> tuple[Optional[str], str]:
        """
        Extract thinking traces from response.
        OLMo 3 Think may use <think>...</think> tags or other delimiters.
        """
        # Check for <think> tags
        if "<think>" in text and "</think>" in text:
            start = text.find("<think>") + len("<think>")
            end = text.find("</think>")
            thinking = text[start:end].strip()
            answer = text[end + len("</think>"):].strip()
            return thinking, answer

        # No explicit thinking markers found
        return None, text

    def save_result(self, result: Dict[str, Any], output_path: str, metadata: Optional[Dict] = None):
        """Save experiment result to JSON file."""
        output = {
            "timestamp": datetime.now().isoformat(),
            "model": self.model,
            "metadata": metadata or {},
            "result": result
        }

        with open(output_path, "w") as f:
            json.dump(output, f, indent=2)

        print(f"✓ Results saved to {output_path}")

    def print_summary(self, result: Dict[str, Any]):
        """Print a human-readable summary of the result."""
        if "error" in result:
            print(f"\n✗ Error: {result['error']}")
            return

        print(f"\n{'='*60}")
        print(f"GENERATION SUMMARY")
        print(f"{'='*60}")
        print(f"Duration: {result['duration_seconds']:.2f} seconds")
        print(f"Prompt tokens: {result['tokens_prompt']:,}")
        print(f"Completion tokens: {result['tokens_completion']:,}")
        print(f"Total tokens: {result['total_tokens']:,}")

        if result['thinking']:
            thinking_len = len(result['thinking'])
            answer_len = len(result['answer'])
            print(f"\nThinking length: {thinking_len:,} chars")
            print(f"Answer length: {answer_len:,} chars")
            print(f"Thinking ratio: {thinking_len / (thinking_len + answer_len) * 100:.1f}%")

        print(f"{'='*60}\n")


if __name__ == "__main__":
    # Test connection
    client = OLMoClient()
    if client.verify_connection():
        print("\nReady for experiments!")
