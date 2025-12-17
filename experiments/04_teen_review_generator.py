#!/usr/bin/env python3
"""
Teen Review Generator - Creates simple A/B comparisons from AI judge results

Takes AI judge rankings and generates lightweight comparison sheets for teen reviewers.
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple


def load_ai_judge_results(results_file: Path) -> Dict:
    """Load AI judge results"""
    with open(results_file, 'r') as f:
        return json.load(f)


def load_story_text(experiment_id: str, results_dir: Path) -> str:
    """Load the story text from an experiment result file"""
    # Map experiment IDs to their result files
    file_mapping = {
        "01_bart_test_20251204_211238": "01_bart_test_20251204_211238.json",
        "02a_temp_0.5_20251207_090043": "02a_temp_0.5_20251207_090043.json",
        "02b_temp_1.0_20251207_090153": "02b_temp_1.0_20251207_090153.json",
        "02c_natural_constraint_20251207_090308": "02c_natural_constraint_20251207_090308.json",
        "02d_style_anchor_20251207_090355": "02d_style_anchor_20251207_090355.json",
    }

    result_file = results_dir / file_mapping.get(experiment_id, f"{experiment_id}.json")

    if not result_file.exists():
        return "[Story text not found]"

    with open(result_file, 'r') as f:
        data = json.load(f)

    response = data['result']['response']

    # Remove thinking traces if present
    if '<think>' in response and '</think>' in response:
        response = response.split('</think>')[-1].strip()

    return response


def get_top_finalists(ai_results: Dict, top_n: int = 2) -> List[Tuple[str, float]]:
    """Get the top N experiments from AI judge rankings"""
    ranking = ai_results["analysis"]["ranking"]
    return ranking[:top_n]


def get_experiment_name(experiment_id: str) -> str:
    """Convert experiment ID to readable name"""
    name_mapping = {
        "01_bart_test_20251204_211238": "Baseline (Temp 0.7)",
        "02a_temp_0.5_20251207_090043": "Lower Temperature (0.5)",
        "02b_temp_1.0_20251207_090153": "Higher Temperature (1.0)",
        "02c_natural_constraint_20251207_090308": "Natural Constraint (max 5 slang)",
        "02d_style_anchor_20251207_090355": "Style Anchor (texting friend)",
    }
    return name_mapping.get(experiment_id, experiment_id)


def generate_markdown_comparison(
    finalist_a: Tuple[str, float],
    finalist_b: Tuple[str, float],
    results_dir: Path
) -> str:
    """Generate a markdown comparison sheet for teens"""

    exp_a_id, score_a = finalist_a
    exp_b_id, score_b = finalist_b

    story_a = load_story_text(exp_a_id, results_dir)
    story_b = load_story_text(exp_b_id, results_dir)

    name_a = get_experiment_name(exp_a_id)
    name_b = get_experiment_name(exp_b_id)

    markdown = f"""# Teen Review: Top 2 Finalists

The AI judges picked these two as the best. Which one feels more natural to you?

**⏱️ Time estimate**: 5 minutes

---

## Story A: {name_a}

{story_a}

---

## Story B: {name_b}

{story_b}

---

## Your Review

**Which one feels more natural?** (Circle one)

- [ ] Story A
- [ ] Story B
- [ ] About the same / can't decide

**Quick thoughts** (optional - anything that stood out to you?):

```
[Your notes here]
```

---

## AI Judge Scores (for reference)

- **Story A ({name_a})**: {score_a:.1f}/10 average
- **Story B ({name_b})**: {score_b:.1f}/10 average

*Note: These are AI opinions - your human judgment is what matters!*
"""

    return markdown


def generate_full_ranking_review(ai_results: Dict, results_dir: Path) -> str:
    """Generate a full ranking sheet showing all 5 experiments"""

    ranking = ai_results["analysis"]["ranking"]

    markdown = """# Teen Review: Full Rankings

The AI judges ranked all 5 experiments. Rate each one quickly (1-10) on overall vibe.

**⏱️ Time estimate**: 10 minutes

---

"""

    for i, (exp_id, ai_score) in enumerate(ranking, 1):
        name = get_experiment_name(exp_id)
        story = load_story_text(exp_id, results_dir)

        markdown += f"""## #{i}: {name}

**AI Score**: {ai_score:.1f}/10

{story}

**Your Score (1-10)**: ____

**Quick vibe check**: Does it feel natural or forced?
- [ ] Natural
- [ ] Forced
- [ ] Somewhere in between

---

"""

    markdown += """## Summary

Your top 3 (ranked):
1. _________________
2. _________________
3. _________________

Any overall thoughts?
```
[Your notes here]
```
"""

    return markdown


def main():
    """Generate teen review sheets from AI judge results"""
    print("📋 Teen Review Generator")
    print("=" * 50)

    # Find the most recent AI judge results
    results_dir = Path(__file__).parent.parent / "results"
    judge_files = sorted(results_dir.glob("03_ai_judges_*.json"))

    if not judge_files:
        print("❌ No AI judge results found. Run 03_ai_judges.py first.")
        return

    latest_results = judge_files[-1]
    print(f"📁 Loading: {latest_results.name}")

    # Load results
    ai_results = load_ai_judge_results(latest_results)

    # Get top 2 finalists
    finalists = get_top_finalists(ai_results, top_n=2)
    print(f"\n🏆 Top 2 finalists:")
    for i, (exp_id, score) in enumerate(finalists, 1):
        print(f"  {i}. {get_experiment_name(exp_id)} ({score:.1f}/10)")

    # Generate comparison sheet
    print("\n📝 Generating comparison sheet...")
    comparison = generate_markdown_comparison(finalists[0], finalists[1], results_dir)

    comparison_file = results_dir / "teen_review_top2_comparison.md"
    with open(comparison_file, 'w') as f:
        f.write(comparison)

    print(f"✅ Saved: {comparison_file}")

    # Generate full ranking sheet
    print("\n📝 Generating full ranking sheet...")
    full_ranking = generate_full_ranking_review(ai_results, results_dir)

    ranking_file = results_dir / "teen_review_full_ranking.md"
    with open(ranking_file, 'w') as f:
        f.write(full_ranking)

    print(f"✅ Saved: {ranking_file}")

    print("\n" + "=" * 50)
    print("✅ Review sheets ready!")
    print("\nNext steps:")
    print("1. Share the comparison file with your kids (5 min)")
    print("2. Optional: Use full ranking if they want to rate all 5 (10 min)")
    print("3. Run analysis script to combine AI + human scores")


if __name__ == "__main__":
    main()
