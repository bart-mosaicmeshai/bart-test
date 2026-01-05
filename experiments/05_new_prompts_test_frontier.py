#!/usr/bin/env python3
"""
Experiment 05: Refined Prompts Test - FRONTIER MODELS ONLY
Testing clearer, humor-focused scenarios at ~50-60 words with frontier models (API only)

Key changes from Experiment 04:
- Explicit humor goal in prompts (aligns with Humor Level rubric)
- Tighter word count (~50-60 vs 50-100)
- Clearer expectations ("clear and makes sense to teenage reader")
- Addresses coherence issues from Experiment 04

New prompts:
- Scenario A: Write a funny story about something crazy that happened at lunch
- Scenario B: Hype up your friend with funny, celebratory message

Goal: Test if clearer, shorter, humor-focused prompts produce outputs that pass
the "good use of slang/emojis, not cringy" validation target.

Models (this script):
1. GPT-5.2 (OpenAI API)
2. Claude Opus 4.5 (Anthropic API)
3. Gemini 3 Pro (Google API) - May be blocked by recitation filter

Note: Run 05_new_prompts_test_llama.py, 05_new_prompts_test_qwen.py, or
05_new_prompts_test_olmo.py to test local models via LM Studio.
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

# Experiment 05: Refined prompts
SCENARIO_A = """Write a ~50-60 word story about something crazy that happened at lunch today. Use Gen-Alpha slang and emojis to make it funny and engaging. Make sure the story is clear and makes sense to the teenage reader."""

SCENARIO_B = """Write a ~50-60 word message hyping up your friend who just got a really good grade. Use Gen-Alpha slang and emojis to make it funny and celebratory. Make sure it's genuinely supportive and makes sense to the teenage reader."""


def test_gpt52(prompt: str, scenario_name: str) -> Dict:
    """Test GPT-5.2 with refined prompt"""
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
        max_completion_tokens=200  # Tighter limit for ~50-60 words
    )

    duration = time.time() - start_time

    result = {
        "model": "GPT-5.2",
        "model_id": "gpt-5.2",
        "scenario": scenario_name,
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 200,
        "response": response.choices[0].message.content,
        "tokens": response.usage.completion_tokens,
        "word_count": len(response.choices[0].message.content.split()),
        "duration_seconds": round(duration, 2),
        "timestamp": datetime.now().isoformat()
    }

    print(f"✅ {result['tokens']} tokens, {result['word_count']} words, {result['duration_seconds']}s")
    return result


def test_claude(prompt: str, scenario_name: str) -> Dict:
    """Test Claude Opus 4.5 with refined prompt"""
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
        max_tokens=200,  # Tighter limit for ~50-60 words
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
        "max_tokens": 200,
        "response": response.content[0].text,
        "tokens": response.usage.output_tokens,
        "word_count": len(response.content[0].text.split()),
        "duration_seconds": round(duration, 2),
        "timestamp": datetime.now().isoformat()
    }

    print(f"✅ {result['tokens']} tokens, {result['word_count']} words, {result['duration_seconds']}s")
    return result


def test_gemini(prompt: str, scenario_name: str) -> Dict:
    """Test Gemini 3 Pro with refined prompt"""
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
        max_output_tokens=200,  # Tighter limit for ~50-60 words
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
        "temperature": 0.9,
        "max_tokens": 200,
        "response": response.text,
        "tokens": word_count,  # Approximate
        "word_count": word_count,
        "duration_seconds": round(duration, 2),
        "timestamp": datetime.now().isoformat()
    }

    print(f"✅ ~{result['tokens']} tokens, {result['word_count']} words, {result['duration_seconds']}s")
    return result


def save_result(result: Dict, filename: str):
    """Save result to JSON"""
    results_dir = Path(__file__).parent.parent / "results"
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
    print(f"Word count: {result['word_count']} (target: ~50-60)")
    print(f"Tokens: {result['tokens']}")
    print(f"Duration: {result['duration_seconds']}s")
    print("\n" + "-" * 70)
    print("RESPONSE:")
    print("-" * 70)
    print(result['response'])
    print()


def main():
    """Run Experiment 05: Refined Prompts Test"""
    print("=" * 70)
    print("EXPERIMENT 05: REFINED PROMPTS TEST - FRONTIER MODELS")
    print("=" * 70)
    print("\nTesting clearer, humor-focused scenarios at ~50-60 words")
    print("Goal: Validate 'good use of slang/emojis, not cringy'\n")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results = []

    scenarios = [
        ("Scenario A - Lunch Story", SCENARIO_A),
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
                    save_result(result, f"05_gpt52_{scenario_name.lower().replace(' ', '_').replace('-', '')}_{timestamp}.json")
            except Exception as e:
                print(f"⚠️  GPT-5.2 test failed: {str(e)}")

        # Claude Opus 4.5
        if CLAUDE_AVAILABLE and os.environ.get("ANTHROPIC_API_KEY"):
            try:
                result = test_claude(prompt, scenario_name)
                if "error" not in result:
                    results.append(result)
                    print_result(result)
                    save_result(result, f"05_claude_{scenario_name.lower().replace(' ', '_').replace('-', '')}_{timestamp}.json")
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
                    save_result(result, f"05_gemini_{scenario_name.lower().replace(' ', '_').replace('-', '')}_{timestamp}.json")
            except Exception as e:
                print(f"⚠️  Gemini test failed: {str(e)}")

    # Summary
    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)
    print(f"\nTotal outputs generated: {len(results)}")
    print("\nWord count check (target: ~50-60 words):\n")

    for result in results:
        wc = result['word_count']
        status = "✅" if 45 <= wc <= 65 else "⚠️"
        print(f"{status} {result['model']:20s} | {result['scenario']:30s} | {wc:3d} words")

    print("\n" + "=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    print("\n1. Run local model tests:")
    print("   - python experiments/05_new_prompts_test_llama.py")
    print("   - python experiments/05_new_prompts_test_qwen.py")
    print("   - python experiments/05_new_prompts_test_olmo.py")
    print("\n2. Review all outputs - do they pass 'not cringy' test?")
    print("3. If yes → create evaluation sheet for judges J and R")
    print("4. If no → diagnose issues and iterate\n")


if __name__ == "__main__":
    main()
