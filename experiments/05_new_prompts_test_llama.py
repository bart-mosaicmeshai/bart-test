#!/usr/bin/env python3
"""
Experiment 05: Refined Prompts Test - LLAMA 3.1 8B ONLY
Testing clearer, humor-focused scenarios at ~50-60 words

Model: Llama 3.1 8B Instruct (Local via LM Studio - MUST BE LOADED FIRST)

Prerequisites:
1. LM Studio running at http://localhost:1234
2. Load meta-llama-3.1-8b-instruct model in LM Studio
3. Run this script

Note: For API models, run 05_new_prompts_test_frontier.py
Note: For other local models, run 05_new_prompts_test_qwen.py or 05_new_prompts_test_olmo.py
"""

import json
import requests
import time
from datetime import datetime
from pathlib import Path
from typing import Dict

# Experiment 05: Refined prompts
SCENARIO_A = """Write a ~50-60 word story about something crazy that happened at lunch today. Use Gen-Alpha slang and emojis to make it funny and engaging. Make sure the story is clear and makes sense to the teenage reader."""

SCENARIO_B = """Write a ~50-60 word message hyping up your friend who just got a really good grade. Use Gen-Alpha slang and emojis to make it funny and celebratory. Make sure it's genuinely supportive and makes sense to the teenage reader."""


def test_llama(prompt: str, scenario_name: str) -> Dict:
    """Test Llama 3.1 8B via LM Studio"""
    print(f"\n🤖 Testing Llama 3.1 8B - {scenario_name}...")
    start_time = time.time()

    try:
        response = requests.post(
            "http://localhost:1234/v1/chat/completions",
            json={
                "model": "meta-llama-3.1-8b-instruct",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 200  # Tighter limit for ~50-60 words
            },
            timeout=120
        )
        response.raise_for_status()
        data = response.json()

        duration = time.time() - start_time
        content = data['choices'][0]['message']['content']

        result = {
            "model": "Llama 3.1 8B Instruct",
            "model_id": "meta-llama-3.1-8b-instruct",
            "scenario": scenario_name,
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 200,
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
    """Run Experiment 05: Llama 3.1 8B Test"""
    print("=" * 70)
    print("EXPERIMENT 05: REFINED PROMPTS TEST - LLAMA 3.1 8B")
    print("=" * 70)
    print("\nPrerequisite: LM Studio running with meta-llama-3.1-8b-instruct loaded")
    print("Testing clearer, humor-focused scenarios at ~50-60 words\n")

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results = []

    scenarios = [
        ("Scenario A - Lunch Story", SCENARIO_A),
        ("Scenario B - Hype Friend", SCENARIO_B)
    ]

    # Test each scenario
    for scenario_name, prompt in scenarios:
        print("\n" + "=" * 70)
        print(f"TESTING: {scenario_name}")
        print("=" * 70)
        print(f"\nPrompt: {prompt}\n")

        result = test_llama(prompt, scenario_name)
        if "error" in result:
            print(f"❌ Test failed: {result['error']}")
            print("\n⚠️  Make sure:")
            print("   1. LM Studio is running at http://localhost:1234")
            print("   2. meta-llama-3.1-8b-instruct model is loaded")
            continue

        results.append(result)
        print_result(result)
        save_result(result, f"05_llama_{scenario_name.lower().replace(' ', '_').replace('-', '')}_{timestamp}.json")

    # Summary
    if results:
        print("\n" + "=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        print(f"\nOutputs generated: {len(results)}")
        print("\nWord count check (target: ~50-60 words):\n")

        for result in results:
            wc = result['word_count']
            status = "✅" if 45 <= wc <= 65 else "⚠️"
            print(f"{status} {result['scenario']:30s} | {wc:3d} words")


if __name__ == "__main__":
    main()
