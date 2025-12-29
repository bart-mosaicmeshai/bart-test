#!/usr/bin/env python3
"""
Experiment 04: New Prompts Validation Test - FRONTIER MODELS ONLY
Testing short, relatable scenarios with frontier models (API only)

New prompts:
- Scenario A: Text your group chat about what happened at lunch today
- Scenario B: Hype up your friend who just got a good grade

Goal: Validate outputs are ~50-100 words and judgeable by teens before designing paper sheet.

Models (this script):
1. GPT-5.2 (OpenAI API)
2. Claude Opus 4.5 (Anthropic API)
3. Gemini 3 Pro (Google API) - NOTE: Blocked by recitation filter (finish_reason=2)

Finding: Gemini 3 Pro refuses to generate Gen-Alpha slang content due to aggressive
recitation filters. This is documented as a key finding about model safety filters
vs. cultural fluency tasks.

Note: Run 04_new_prompts_test_llama.py or 04_new_prompts_test_olmo.py to test local models
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
    print("⚠️  Anthropic package not found")

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("⚠️  OpenAI package not found")

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    print("⚠️  Google GenAI package not found")

# For local models via LM Studio
import requests

# The new prompts
SCENARIO_A = """Text your group chat about what happened at lunch today using Gen-Alpha slang and emojis. Keep it short (50-100 words max)."""

SCENARIO_B = """Hype up your friend who just got a good grade using Gen-Alpha slang and emojis. Keep it short (50-100 words max)."""


def test_gpt52(prompt: str, scenario_name: str) -> Dict:
    """Test GPT-5.2 with new prompt"""
    if not OPENAI_AVAILABLE:
        return {"error": "OpenAI package not available"}

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return {"error": "OPENAI_API_KEY not set"}

    print(f"\n🤖 Testing GPT-5.2 - {scenario_name}...")
    start_time = time.time()

    client = OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model="gpt-5.2",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_completion_tokens=300  # Short outputs
    )

    duration = time.time() - start_time

    result = {
        "model": "GPT-5.2",
        "model_id": "gpt-5.2",
        "scenario": scenario_name,
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 300,
        "response": response.choices[0].message.content,
        "tokens": response.usage.completion_tokens,
        "word_count": len(response.choices[0].message.content.split()),
        "duration_seconds": round(duration, 2),
        "timestamp": datetime.now().isoformat()
    }

    print(f"✅ {result['tokens']} tokens, {result['word_count']} words, {result['duration_seconds']}s")
    return result


def test_claude(prompt: str, scenario_name: str) -> Dict:
    """Test Claude Opus 4.5 with new prompt"""
    if not CLAUDE_AVAILABLE:
        return {"error": "Anthropic package not available"}

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return {"error": "ANTHROPIC_API_KEY not set"}

    print(f"\n🤖 Testing Claude Opus 4.5 - {scenario_name}...")
    start_time = time.time()

    client = Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=300,
        temperature=0.7,
        messages=[{"role": "user", "content": prompt}]
    )

    duration = time.time() - start_time

    result = {
        "model": "Claude Opus 4.5",
        "model_id": "claude-opus-4-5-20251101",
        "scenario": scenario_name,
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 300,
        "response": response.content[0].text,
        "tokens": response.usage.output_tokens,
        "word_count": len(response.content[0].text.split()),
        "duration_seconds": round(duration, 2),
        "timestamp": datetime.now().isoformat()
    }

    print(f"✅ {result['tokens']} tokens, {result['word_count']} words, {result['duration_seconds']}s")
    return result


def test_gemini(prompt: str, scenario_name: str) -> Dict:
    """Test Gemini 3 Pro with new prompt"""
    if not GEMINI_AVAILABLE:
        return {"error": "Google GenAI package not available"}

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        return {"error": "GOOGLE_API_KEY not set"}

    print(f"\n🤖 Testing Gemini 3 Pro - {scenario_name}...")
    start_time = time.time()

    genai.configure(api_key=api_key)

    # Disable safety filters for slang/casual language
    from google.generativeai.types import HarmCategory, HarmBlockThreshold

    safety_settings = {
        HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    }

    model = genai.GenerativeModel(
        'gemini-3-pro-preview',
        system_instruction="You are a creative writer. Generate completely original responses in your own unique voice. Avoid any memorized phrases or common patterns."
    )

    generation_config = genai.GenerationConfig(
        temperature=0.9,  # Higher temperature for more originality
        max_output_tokens=300,
        top_p=0.95,
        top_k=40
    )

    response = model.generate_content(
        prompt,
        generation_config=generation_config,
        safety_settings=safety_settings
    )
    duration = time.time() - start_time

    # Check if response was blocked
    if not response.candidates or not response.candidates[0].content.parts:
        return {
            "error": f"Gemini blocked response. Finish reason: {response.candidates[0].finish_reason if response.candidates else 'No candidates'}",
            "safety_ratings": str(response.candidates[0].safety_ratings if response.candidates else 'None')
        }

    word_count = len(response.text.split())

    result = {
        "model": "Gemini 3 Pro",
        "model_id": "gemini-3-pro-preview",
        "scenario": scenario_name,
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 300,
        "response": response.text,
        "tokens": word_count,  # Approximate
        "word_count": word_count,
        "duration_seconds": round(duration, 2),
        "timestamp": datetime.now().isoformat()
    }

    print(f"✅ ~{result['tokens']} tokens, {result['word_count']} words, {result['duration_seconds']}s")
    return result


def test_local_model(prompt: str, scenario_name: str, model_name: str, model_id: str) -> Dict:
    """Test local model via LM Studio"""
    print(f"\n🤖 Testing {model_name} - {scenario_name}...")
    start_time = time.time()

    try:
        response = requests.post(
            "http://localhost:1234/v1/chat/completions",
            json={
                "model": model_id,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 300
            },
            timeout=120
        )
        response.raise_for_status()
        data = response.json()

        duration = time.time() - start_time
        content = data['choices'][0]['message']['content']

        result = {
            "model": model_name,
            "model_id": model_id,
            "scenario": scenario_name,
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 300,
            "response": content,
            "tokens": data['usage']['completion_tokens'],
            "word_count": len(content.split()),
            "duration_seconds": round(duration, 2),
            "timestamp": datetime.now().isoformat()
        }

        print(f"✅ {result['tokens']} tokens, {result['word_count']} words, {result['duration_seconds']}s")
        return result

    except Exception as e:
        return {"error": f"Local model error: {str(e)}"}


def save_result(result: Dict, filename: str):
    """Save result to JSON"""
    results_dir = Path(__file__).parent.parent / "results" / "04_experiment_runs"
    results_dir.mkdir(parents=True, exist_ok=True)
    filepath = results_dir / filename

    with open(filepath, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"💾 Saved to: {filepath}")


def print_result(result: Dict):
    """Print result summary"""
    if "error" in result:
        print(f"❌ Error: {result['error']}")
        return

    print("\n" + "=" * 70)
    print(f"MODEL: {result['model']}")
    print(f"SCENARIO: {result['scenario']}")
    print("=" * 70)
    print(f"Word count: {result['word_count']} (target: 50-100)")
    print(f"Tokens: {result['tokens']}")
    print(f"Duration: {result['duration_seconds']}s")
    print("\n" + "-" * 70)
    print("RESPONSE:")
    print("-" * 70)
    print(result['response'])
    print()


def main():
    """Run Experiment 04: New Prompts Validation"""
    print("=" * 70)
    print("EXPERIMENT 04: NEW PROMPTS VALIDATION TEST")
    print("=" * 70)
    print("\nTesting short, relatable scenarios with 5 models")
    print("Goal: Validate outputs are ~50-100 words\n")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results = []

    scenarios = [
        ("Scenario A - Group Chat", SCENARIO_A),
        ("Scenario B - Hype Friend", SCENARIO_B)
    ]

    # Test each scenario with each model
    for scenario_name, prompt in scenarios:
        print("\n" + "=" * 70)
        print(f"TESTING: {scenario_name}")
        print("=" * 70)
        print(f"\nPrompt: {prompt}\n")

        # GPT-5.2
        if OPENAI_AVAILABLE and os.environ.get("OPENAI_API_KEY"):
            try:
                result = test_gpt52(prompt, scenario_name)
                if "error" not in result:
                    results.append(result)
                    print_result(result)
                    save_result(result, f"04_gpt52_{scenario_name.lower().replace(' ', '_').replace('-', '')}_{timestamp}.json")
            except Exception as e:
                print(f"⚠️  GPT-5.2 test failed: {str(e)}")

        # Claude Opus 4.5
        if CLAUDE_AVAILABLE and os.environ.get("ANTHROPIC_API_KEY"):
            try:
                result = test_claude(prompt, scenario_name)
                if "error" not in result:
                    results.append(result)
                    print_result(result)
                    save_result(result, f"04_claude_{scenario_name.lower().replace(' ', '_').replace('-', '')}_{timestamp}.json")
            except Exception as e:
                print(f"⚠️  Claude test failed: {str(e)}")

        # Gemini 3 Pro
        if GEMINI_AVAILABLE and os.environ.get("GOOGLE_API_KEY"):
            try:
                result = test_gemini(prompt, scenario_name)
                if "error" in result:
                    print(f"⚠️  Gemini test failed: {result['error']}")
                    if 'safety_ratings' in result:
                        print(f"    Safety ratings: {result['safety_ratings']}")
                else:
                    results.append(result)
                    print_result(result)
                    save_result(result, f"04_gemini_{scenario_name.lower().replace(' ', '_').replace('-', '')}_{timestamp}.json")
            except Exception as e:
                print(f"⚠️  Gemini test failed: {str(e)}")

        # No local models in this script - frontier models only

    # Summary
    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    print(f"\nTotal outputs generated: {len(results)}")
    print("\nWord count check (target: 50-100 words):\n")

    for result in results:
        wc = result['word_count']
        status = "✅" if 50 <= wc <= 100 else "⚠️"
        print(f"{status} {result['model']:20s} | {result['scenario']:30s} | {wc:3d} words")

    print("\n" + "=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    print("\n1. Review outputs - are they judgeable by teens?")
    print("2. Check word counts - mostly in 50-100 range?")
    print("3. If yes → design paper evaluation sheet")
    print("4. If no → adjust prompts and retest\n")


if __name__ == "__main__":
    main()
