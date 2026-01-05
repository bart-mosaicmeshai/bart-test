#!/usr/bin/env python3
"""
Experiment 05: Refined Prompts Test - OLMO 3 32B THINK ONLY
Testing clearer, humor-focused scenarios at ~50-60 words

Model: OLMo 3 32B Think (Local via LM Studio - MUST BE LOADED FIRST)
Note: This is a REASONING MODEL - produces extensive thinking traces

Prerequisites:
1. LM Studio running at http://localhost:1234
2. Load allenai/olmo-3-32b-think model in LM Studio
3. Run this script

WARNING: This model is SLOW (~30-60 seconds per output) and produces extensive
thinking traces. Actual output must be extracted after </think> tag.
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


def test_olmo(prompt: str, scenario_name: str) -> Dict:
    """Test OLMo 3 32B Think via LM Studio"""
    print(f"\n🤖 Testing OLMo 3 32B Think - {scenario_name}...")
    print("⚠️  This may take 30-60 seconds...")
    start_time = time.time()

    try:
        response = requests.post(
            "http://localhost:1234/v1/chat/completions",
            json={
                "model": "allenai/olmo-3-32b-think",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.7,
                "max_tokens": 1500  # Reasoning model needs lots of tokens (thinking + output)
            },
            timeout=180  # Longer timeout for slow model
        )
        response.raise_for_status()
        data = response.json()

        duration = time.time() - start_time
        content = data['choices'][0]['message']['content']

        # Extract actual output after </think> tag
        actual_output = content
        if '</think>' in content:
            actual_output = content.split('</think>')[-1].strip()

        result = {
            "model": "OLMo 3 32B Think",
            "model_id": "allenai/olmo-3-32b-think",
            "scenario": scenario_name,
            "prompt": prompt,
            "temperature": 0.7,
            "max_tokens": 1500,
            "response": content,  # Full response with thinking
            "actual_output": actual_output,  # Extracted message
            "tokens": data['usage']['completion_tokens'],
            "word_count_total": len(content.split()),
            "word_count_actual": len(actual_output.split()),
            "duration_seconds": round(duration, 2),
            "timestamp": datetime.now().isoformat(),
            "note": "Reasoning model - actual output extracted after </think> tag"
        }

        print(f"✅ {result['tokens']} tokens total, {result['word_count_actual']} words in actual output, {result['duration_seconds']}s")
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
    print(f"Word count (actual output): {result['word_count_actual']} (target: ~50-60)")
    print(f"Tokens (including thinking): {result['tokens']}")
    print(f"Duration: {result['duration_seconds']}s")
    print("\n" + "-" * 70)
    print("ACTUAL OUTPUT (after </think>):")
    print("-" * 70)
    print(result['actual_output'])
    print()


def main():
    """Run Experiment 05: OLMo 3 32B Think Test"""
    print("=" * 70)
    print("EXPERIMENT 05: REFINED PROMPTS TEST - OLMO 3 32B THINK (REASONING MODEL)")
    print("=" * 70)
    print("\nPrerequisite: LM Studio running with allenai/olmo-3-32b-think loaded")
    print("Testing clearer, humor-focused scenarios at ~50-60 words\n")
    print("⚠️  WARNING: This model is VERY SLOW (~30-60 seconds per output)")
    print("Note: This model produces extensive <think> tags. Actual output is extracted.\n")

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

        result = test_olmo(prompt, scenario_name)
        if "error" in result:
            print(f"❌ Test failed: {result['error']}")
            print("\n⚠️  Make sure:")
            print("   1. LM Studio is running at http://localhost:1234")
            print("   2. allenai/olmo-3-32b-think model is loaded")
            continue

        results.append(result)
        print_result(result)
        save_result(result, f"05_olmo3_{scenario_name.lower().replace(' ', '_').replace('-', '')}_{timestamp}.json")

    # Summary
    if results:
        print("\n" + "=" * 70)
        print("TEST SUMMARY")
        print("=" * 70)
        print(f"\nOutputs generated: {len(results)}")
        print("\nWord count check (target: ~50-60 words in actual output):\n")

        for result in results:
            wc = result['word_count_actual']
            status = "✅" if 45 <= wc <= 65 else "⚠️"
            print(f"{status} {result['scenario']:30s} | {wc:3d} words")


if __name__ == "__main__":
    main()
