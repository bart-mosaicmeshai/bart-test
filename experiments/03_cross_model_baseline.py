#!/usr/bin/env python3
"""
Experiment 03: Cross-Model Baseline Test
Testing GPT-4o, Claude 3.5 Sonnet, and Gemini Pro with the EXACT baseline prompt.

Goal: Determine if the "trying too hard" problem is prompt-related or model-specific.
Decision point: If all 3 models struggle, consider modifying prompt. If 1-2 handle it well, lock baseline.
"""

import json
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

# API clients
try:
    from anthropic import Anthropic
    CLAUDE_AVAILABLE = True
except ImportError:
    CLAUDE_AVAILABLE = False
    print("⚠️  Anthropic package not found. Install with: pip install anthropic")

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("⚠️  OpenAI package not found. Install with: pip install openai")

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("⚠️  Google GenAI package not found. Install with: pip install google-generativeai")


# The exact baseline prompt from Experiment 01
BASELINE_PROMPT = """Tell the story of a developer deploying code to production on a Friday afternoon (and something goes wrong) using Gen-Alpha slang and emojis. Make it realistic and funny."""


def test_gpt4o(prompt: str) -> Dict:
    """Test GPT-4o with the baseline prompt"""
    if not OPENAI_AVAILABLE:
        return {"error": "OpenAI package not available"}

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OPENAI_API_KEY environment variable not set"}

    print("\n🤖 Testing GPT-5.2...")
    start_time = time.time()

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-5.2",
        messages=[{
            "role": "user",
            "content": prompt
        }],
        temperature=0.7,
        max_completion_tokens=8192
    )

    duration = time.time() - start_time

    result = {
        "model": "GPT-5.2",
        "model_id": "gpt-5.2",
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 8192,
        "response": response.choices[0].message.content,
        "tokens": response.usage.completion_tokens,
        "duration_seconds": round(duration, 2),
        "timestamp": datetime.now().isoformat()
    }

    print(f"✅ Generated {result['tokens']} tokens in {result['duration_seconds']}s")

    return result


def test_claude(prompt: str) -> Dict:
    """Test Claude 3.5 Sonnet with the baseline prompt"""
    if not CLAUDE_AVAILABLE:
        return {"error": "Anthropic package not available"}

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return {"error": "ANTHROPIC_API_KEY environment variable not set"}

    print("\n🤖 Testing Claude Opus 4.5...")
    start_time = time.time()

    client = Anthropic(api_key=api_key)

    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=8192,
        temperature=0.7,
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    duration = time.time() - start_time

    result = {
        "model": "Claude Opus 4.5",
        "model_id": "claude-opus-4-5-20251101",
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 8192,
        "response": response.content[0].text,
        "tokens": response.usage.output_tokens,
        "duration_seconds": round(duration, 2),
        "timestamp": datetime.now().isoformat()
    }

    print(f"✅ Generated {result['tokens']} tokens in {result['duration_seconds']}s")

    return result


def test_gemini(prompt: str) -> Dict:
    """Test Gemini Pro with the baseline prompt"""
    if not GEMINI_AVAILABLE:
        return {"error": "Google GenAI package not available"}

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return {"error": "GOOGLE_API_KEY environment variable not set"}

    print("\n🤖 Testing Gemini 3 Pro...")
    start_time = time.time()

    genai.configure(api_key=api_key)

    # Use gemini-3-pro-preview (most powerful Gemini 3 model)
    model = genai.GenerativeModel('gemini-3-pro-preview')

    # Gemini uses generation_config for temperature
    generation_config = genai.GenerationConfig(
        temperature=0.7,
        max_output_tokens=8192,
    )

    response = model.generate_content(prompt, generation_config=generation_config)

    duration = time.time() - start_time

    # Gemini doesn't always provide token count in response
    tokens = len(response.text.split())  # Rough approximation

    result = {
        "model": "Gemini 3 Pro",
        "model_id": "gemini-3-pro-preview",
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 8192,
        "response": response.text,
        "tokens": tokens,
        "tokens_note": "Approximate word count (Gemini doesn't provide token count)",
        "duration_seconds": round(duration, 2),
        "timestamp": datetime.now().isoformat()
    }

    print(f"✅ Generated ~{result['tokens']} tokens in {result['duration_seconds']}s")

    return result


def save_result(result: Dict, filename: str):
    """Save a result to JSON file"""
    results_dir = Path(__file__).parent.parent / "results"
    results_dir.mkdir(exist_ok=True)

    filepath = results_dir / filename

    with open(filepath, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"💾 Saved to: {filepath}")


def print_result(result: Dict):
    """Print a result summary"""
    if "error" in result:
        print(f"❌ Error: {result['error']}")
        return

    print("\n" + "=" * 70)
    print(f"MODEL: {result['model']}")
    print("=" * 70)
    print(f"\nTokens: {result['tokens']}")
    print(f"Duration: {result['duration_seconds']}s")
    print("\n" + "-" * 70)
    print("RESPONSE:")
    print("-" * 70)
    print(result['response'])
    print()


def main():
    """Run Experiment 03: Cross-Model Baseline Test"""
    print("=" * 70)
    print("EXPERIMENT 03: CROSS-MODEL BASELINE TEST")
    print("=" * 70)
    print("\nTesting frontier models with the EXACT baseline prompt")
    print("Goal: Determine if 'trying too hard' is prompt or model issue")
    print()

    print("=" * 70)
    print("THE PROMPT")
    print("=" * 70)
    print(f"\n{BASELINE_PROMPT}\n")

    # Check which models are available
    available_models = []
    if OPENAI_AVAILABLE and os.environ.get("OPENAI_API_KEY"):
        available_models.append("GPT-5.2")
    if CLAUDE_AVAILABLE and os.environ.get("ANTHROPIC_API_KEY"):
        available_models.append("Claude Opus 4.5")
    if GEMINI_AVAILABLE and os.environ.get("GOOGLE_API_KEY"):
        available_models.append("Gemini 3 Pro")

    if not available_models:
        print("❌ No models available. Please install packages and set API keys:")
        print("  - pip install openai anthropic google-generativeai")
        print("  - Set OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY")
        return

    print(f"✅ Available models: {', '.join(available_models)}")
    print()

    # Run tests
    results = {}
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Test GPT-5.2
    if "GPT-5.2" in available_models:
        result = test_gpt4o(BASELINE_PROMPT)
        results["gpt4o"] = result
        if "error" not in result:
            print_result(result)
            save_result(result, f"03a_gpt4o_baseline_{timestamp}.json")

    # Test Claude Opus 4.5
    if "Claude Opus 4.5" in available_models:
        result = test_claude(BASELINE_PROMPT)
        results["claude"] = result
        if "error" not in result:
            print_result(result)
            save_result(result, f"03b_claude_baseline_{timestamp}.json")

    # Test Gemini 3 Pro
    if "Gemini 3 Pro" in available_models:
        result = test_gemini(BASELINE_PROMPT)
        results["gemini"] = result
        if "error" not in result:
            print_result(result)
            save_result(result, f"03c_gemini_baseline_{timestamp}.json")

    # Summary comparison
    print("\n" + "=" * 70)
    print("COMPARISON SUMMARY")
    print("=" * 70)
    print()

    # OLMo baseline for reference
    print("OLMo 3 32B Think (Baseline): 1,060 tokens, 44s")

    for model_key, result in results.items():
        if "error" not in result:
            print(f"{result['model']}: {result['tokens']} tokens, {result['duration_seconds']}s")

    print()
    print("=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    print()
    print("1. Review outputs above - do they 'try too hard' like OLMo?")
    print("2. Check for:")
    print("   - Slang density (natural vs forced)")
    print("   - Dated terms ('no cap', 'vibe')")
    print("   - Emoji overuse")
    print("   - Natural code-switching")
    print()
    print("3. Decision point:")
    print("   - If all 3 struggle → Consider modifying prompt")
    print("   - If 1-2 handle it well → Lock baseline as canonical")
    print()
    print("4. Run AI judges on these outputs:")
    print("   python experiments/03_ai_judges.py")
    print()
    print("5. Get teen judge feedback")
    print()


if __name__ == "__main__":
    main()
