#!/usr/bin/env python3
"""
Experiment 02: Constraint Experiments
Testing temperature and prompt variations to reduce "overthinking" effect.

Runs 5 variations:
1. Baseline (temp 0.7, original prompt) - already exists, for comparison
2. Lower temp (0.5) - test if less randomness helps
3. Higher temp (1.0) - test if more randomness helps
4. Natural constraint - limit slang usage explicitly
5. Style anchor - "texting a friend" framing
"""

import sys
import os
from pathlib import Path
from datetime import datetime
import time

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from olmo_client import OLMoClient


# Base prompt
BASE_PROMPT = """Tell the story of a developer deploying code to production on a Friday afternoon (and something goes wrong) using Gen-Alpha slang and emojis. Make it realistic and funny."""

# Experiment configurations
EXPERIMENTS = [
    {
        "id": "02a_temp_0.5",
        "name": "Lower Temperature (0.5)",
        "description": "Test if reduced randomness produces more natural slang usage",
        "temperature": 0.5,
        "prompt": BASE_PROMPT,
        "hypothesis": "Less randomness = more 'correct' but possibly stiffer output"
    },
    {
        "id": "02b_temp_1.0",
        "name": "Higher Temperature (1.0)",
        "description": "Test if increased randomness produces more natural variation",
        "temperature": 1.0,
        "prompt": BASE_PROMPT,
        "hypothesis": "More randomness = more natural, less 'homework-like' variation"
    },
    {
        "id": "02c_natural_constraint",
        "name": "Natural Constraint",
        "description": "Explicitly limit slang usage to prevent cramming",
        "temperature": 0.7,
        "prompt": BASE_PROMPT + " Use slang naturally - max 5 slang terms total.",
        "hypothesis": "Hard limit prevents 'ELA project' effect where AI crams slang"
    },
    {
        "id": "02d_style_anchor",
        "name": "Style Anchor (Texting Friend)",
        "description": "Frame as casual texting to reduce formality",
        "temperature": 0.7,
        "prompt": BASE_PROMPT + " Write like you're texting a friend who codes.",
        "hypothesis": "Social context reduces overthinking and formality"
    }
]


def run_experiment(client: OLMoClient, experiment: dict, output_dir: Path):
    """Run a single experiment configuration."""

    print("\n" + "=" * 70)
    print(f"EXPERIMENT: {experiment['name']}")
    print("=" * 70)
    print(f"\nDescription: {experiment['description']}")
    print(f"Hypothesis: {experiment['hypothesis']}")
    print(f"Temperature: {experiment['temperature']}")
    print(f"\nPrompt:\n{experiment['prompt']}\n")

    # Run inference
    print("⏳ Generating response...")
    result = client.complete(
        prompt=experiment['prompt'],
        temperature=experiment['temperature'],
        max_tokens=8192
    )

    # Print summary
    client.print_summary(result)

    # Print the response
    if "error" not in result:
        print("=" * 70)
        print("RESPONSE")
        print("=" * 70)
        print()
        print(result['answer'])
        print()
    else:
        print(f"\n✗ Error: {result['error']}")
        return None

    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = output_dir / f"{experiment['id']}_{timestamp}.json"

    metadata = {
        "experiment": experiment['id'],
        "name": experiment['name'],
        "description": experiment['description'],
        "hypothesis": experiment['hypothesis'],
        "temperature": experiment['temperature'],
        "prompt": experiment['prompt']
    }

    client.save_result(result, str(output_file), metadata)

    return {
        "experiment_id": experiment['id'],
        "name": experiment['name'],
        "output_file": output_file,
        "tokens": result['tokens_completion'],
        "duration": result['duration_seconds']
    }


def main():
    """Run all constraint experiments."""

    print("=" * 70)
    print("EXPERIMENT 02: CONSTRAINT EXPERIMENTS")
    print("=" * 70)
    print("\nTesting variations to reduce 'overthinking' effect")
    print(f"Running {len(EXPERIMENTS)} experiments on OLMo 3 32B Think\n")

    # Initialize client
    client = OLMoClient()

    # Verify connection
    if not client.verify_connection():
        print("\n✗ Cannot connect to LM Studio. Make sure it's running.")
        return

    # Setup output directory
    output_dir = Path(__file__).parent.parent / "results"
    output_dir.mkdir(exist_ok=True)

    # Run all experiments
    results_summary = []

    for i, experiment in enumerate(EXPERIMENTS, 1):
        print(f"\n{'='*70}")
        print(f"RUNNING EXPERIMENT {i}/{len(EXPERIMENTS)}")
        print(f"{'='*70}")

        result = run_experiment(client, experiment, output_dir)

        if result:
            results_summary.append(result)

        # Brief pause between experiments
        if i < len(EXPERIMENTS):
            print("\n⏸️  Pausing 3 seconds before next experiment...")
            time.sleep(3)

    # Print final summary
    print("\n" + "=" * 70)
    print("ALL EXPERIMENTS COMPLETE")
    print("=" * 70)
    print(f"\nRan {len(results_summary)} experiments successfully:\n")

    for result in results_summary:
        print(f"  {result['name']}")
        print(f"    Tokens: {result['tokens']:,} | Duration: {result['duration']:.1f}s")
        print(f"    File: {result['output_file'].name}\n")

    print("\n" + "=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    print("\n1. Review all responses in the results/ directory")
    print("2. Share with your teen judges for evaluation")
    print("3. Compare which approach reduces 'overthinking' best")
    print("4. Document findings for blog post #2\n")
    print("Compare baseline (01_bart_test_20251204_211238.json) with these results!\n")


if __name__ == "__main__":
    main()
