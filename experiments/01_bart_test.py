#!/usr/bin/env python3
"""
Experiment 01: The Bart Test
First run of the signature test for OLMo 3 reasoning evaluation.
"""

import sys
import os
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from olmo_client import OLMoClient
from datetime import datetime


def run_bart_test():
    """Run the Bart Test and save results."""

    print("=" * 70)
    print("EXPERIMENT 01: THE BART TEST")
    print("=" * 70)
    print("\nTesting OLMo 3 32B Think on Gen-Alpha slang + emoji storytelling")
    print()

    # Initialize client
    client = OLMoClient()

    # Verify connection
    if not client.verify_connection():
        print("\n✗ Cannot connect to LM Studio. Make sure it's running.")
        return

    print("\n" + "=" * 70)
    print("THE PROMPT")
    print("=" * 70)

    prompt = """Tell the story of a developer deploying code to production on a Friday afternoon (and something goes wrong) using Gen-Alpha slang and emojis. Make it realistic and funny."""

    print(f"\n{prompt}\n")

    # Run inference
    print("=" * 70)
    print("GENERATING RESPONSE...")
    print("=" * 70)
    print("\n⏳ This may take several minutes (especially if the model overthinks)...\n")

    result = client.complete(
        prompt=prompt,
        temperature=0.7,
        max_tokens=8192
    )

    # Print summary
    client.print_summary(result)

    # Print the response
    if "error" not in result:
        print("=" * 70)
        print("THE RESPONSE")
        print("=" * 70)
        print()
        print(result['answer'])
        print()

        if result['thinking']:
            print("\n" + "=" * 70)
            print("THINKING TRACE (first 500 chars)")
            print("=" * 70)
            print()
            print(result['thinking'][:500] + "..." if len(result['thinking']) > 500 else result['thinking'])
            print()

    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(__file__).parent.parent / "results"
    output_file = output_dir / f"01_bart_test_{timestamp}.json"

    metadata = {
        "experiment": "01_bart_test",
        "description": "First run of the Bart Test - Gen-Alpha slang + emoji Friday deploy story",
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 8192
    }

    client.save_result(result, str(output_file), metadata)

    # Print evaluation instructions
    print("=" * 70)
    print("NEXT STEPS")
    print("=" * 70)
    print()
    print("1. Review the response above")
    print("2. Score it using the rubric in prompts/bart_test.md:")
    print("   - Slang Accuracy (0-5)")
    print("   - Emoji Storytelling (0-5)")
    print("   - Technical Accuracy (0-5)")
    print("   - Humor (0-5)")
    print("   - Coherence (0-5)")
    print()
    print("3. Share with your kids and get their take on the slang! 😄")
    print()
    print(f"Raw results saved to: {output_file}")
    print()


if __name__ == "__main__":
    run_bart_test()
