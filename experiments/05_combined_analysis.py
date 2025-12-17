#!/usr/bin/env python3
"""
Combined Analysis - Merge AI judge scores with human teen reviews

Analyzes correlation between AI and human judges, identifies disagreements,
and generates final rankings.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional


def load_ai_judge_results(results_dir: Path) -> Optional[Dict]:
    """Load most recent AI judge results"""
    judge_files = sorted(results_dir.glob("03_ai_judges_*.json"))
    if not judge_files:
        return None

    with open(judge_files[-1], 'r') as f:
        return json.load(f)


def load_human_reviews(results_dir: Path) -> Optional[Dict]:
    """Load human teen reviews from markdown files"""
    # This is a placeholder - you'll manually add human scores here
    # after your kids review the outputs

    comparison_file = results_dir / "teen_review_top2_comparison.md"
    ranking_file = results_dir / "teen_review_full_ranking.md"

    # For now, return None - will be filled in after human reviews
    return None


def calculate_correlation(ai_scores: List[float], human_scores: List[float]) -> float:
    """Calculate Pearson correlation between AI and human scores"""
    if len(ai_scores) != len(human_scores) or len(ai_scores) == 0:
        return 0.0

    n = len(ai_scores)
    mean_ai = sum(ai_scores) / n
    mean_human = sum(human_scores) / n

    numerator = sum((ai_scores[i] - mean_ai) * (human_scores[i] - mean_human) for i in range(n))
    denominator_ai = sum((x - mean_ai) ** 2 for x in ai_scores) ** 0.5
    denominator_human = sum((x - mean_human) ** 2 for x in human_scores) ** 0.5

    if denominator_ai == 0 or denominator_human == 0:
        return 0.0

    return numerator / (denominator_ai * denominator_human)


def analyze_agreement(ai_results: Dict, human_reviews: Dict) -> Dict:
    """Analyze where AI and human judges agree/disagree"""

    analysis = {
        "agreement_level": "pending",
        "correlation": None,
        "disagreements": [],
        "consensus_ranking": []
    }

    if not human_reviews:
        return analysis

    # Extract scores
    ai_experiments = ai_results["analysis"]["ranking"]
    human_experiments = human_reviews.get("experiments", [])

    # Calculate correlation if we have matching data
    # (This will be implemented once human review format is defined)

    return analysis


def generate_report(ai_results: Dict, human_reviews: Optional[Dict], output_file: Path):
    """Generate a comprehensive analysis report"""

    report = {
        "timestamp": ai_results["timestamp"],
        "ai_judges": {
            "count": len(ai_results["experiments"][0]["judge_evaluations"]),
            "models": [
                j["judge"] for j in ai_results["experiments"][0]["judge_evaluations"]
                if "error" not in j
            ]
        },
        "rankings": {}
    }

    # AI rankings
    ai_ranking = ai_results["analysis"]["ranking"]
    report["rankings"]["ai_judges"] = [
        {"experiment": exp_id, "score": score}
        for exp_id, score in ai_ranking
    ]

    # Human rankings (if available)
    if human_reviews:
        report["rankings"]["human_judges"] = human_reviews.get("ranking", [])
        report["agreement_analysis"] = analyze_agreement(ai_results, human_reviews)
    else:
        report["rankings"]["human_judges"] = "pending"
        report["agreement_analysis"] = "awaiting human reviews"

    # Detailed scores by category
    report["detailed_scores"] = {}
    for experiment in ai_results["experiments"]:
        exp_id = experiment["experiment_id"]
        agg = ai_results["analysis"]["aggregates"].get(exp_id, {})

        report["detailed_scores"][exp_id] = {
            "overall_vibe": agg.get("overall_vibe", {}),
            "slang_game": agg.get("slang_game", {}),
            "emoji_energy": agg.get("emoji_energy", {}),
            "humor_level": agg.get("humor_level", {}),
            "overall_average": agg.get("overall_average", 0)
        }

    # Save report
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    return report


def print_summary(report: Dict):
    """Print a human-readable summary"""

    print("\n" + "=" * 60)
    print("📊 COMBINED ANALYSIS SUMMARY")
    print("=" * 60)

    # AI Judge Rankings
    print("\n🤖 AI Judge Rankings:")
    for i, item in enumerate(report["rankings"]["ai_judges"], 1):
        exp_name = get_experiment_name(item["experiment"])
        print(f"  {i}. {exp_name}: {item['score']:.2f}/10")

    # Human Rankings
    print("\n👥 Human Judge Rankings:")
    if report["rankings"]["human_judges"] == "pending":
        print("  ⏳ Awaiting teen reviews")
    else:
        for i, item in enumerate(report["rankings"]["human_judges"], 1):
            print(f"  {i}. {item}")

    # Agreement Analysis
    print("\n🔍 Agreement Analysis:")
    if isinstance(report["agreement_analysis"], str):
        print(f"  {report['agreement_analysis']}")
    else:
        agreement = report["agreement_analysis"]
        if agreement.get("correlation") is not None:
            corr = agreement["correlation"]
            print(f"  Correlation: {corr:.3f}", end="")
            if corr > 0.7:
                print(" (Strong agreement ✅)")
            elif corr > 0.4:
                print(" (Moderate agreement ⚠️)")
            else:
                print(" (Weak agreement ❌)")
        else:
            print("  Not enough data yet")

    # Detailed Category Breakdown (for winner)
    print("\n🏆 Top Performer Breakdown:")
    top_exp = report["rankings"]["ai_judges"][0]["experiment"]
    scores = report["detailed_scores"][top_exp]

    categories = {
        "overall_vibe": "Overall Vibe",
        "slang_game": "Slang Game",
        "emoji_energy": "Emoji Energy",
        "humor_level": "Humor Level"
    }

    for key, label in categories.items():
        if key in scores and "mean" in scores[key]:
            mean = scores[key]["mean"]
            print(f"  {label}: {mean:.1f}/10")

    print("\n" + "=" * 60)


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


def main():
    """Run combined analysis"""
    print("📊 Combined Analysis - AI + Human Judges")
    print("=" * 60)

    results_dir = Path(__file__).parent.parent / "results"

    # Load AI judge results
    print("\n📁 Loading AI judge results...")
    ai_results = load_ai_judge_results(results_dir)

    if not ai_results:
        print("❌ No AI judge results found. Run 03_ai_judges.py first.")
        return

    print("✅ AI judge results loaded")

    # Load human reviews (if available)
    print("\n📁 Loading human reviews...")
    human_reviews = load_human_reviews(results_dir)

    if human_reviews:
        print("✅ Human reviews loaded")
    else:
        print("⏳ Human reviews not yet available")

    # Generate combined report
    print("\n📝 Generating analysis report...")
    output_file = results_dir / "combined_analysis.json"
    report = generate_report(ai_results, human_reviews, output_file)

    print(f"✅ Report saved: {output_file}")

    # Print summary
    print_summary(report)

    # Next steps
    print("\n📋 Next Steps:")
    if not human_reviews:
        print("1. Share teen review sheets with your kids")
        print("2. Manually add their scores to this script")
        print("3. Re-run this analysis to see agreement")
    else:
        print("1. Review agreement analysis above")
        print("2. Decide: Trust AI judges for future tests?")
        print("3. Write blog post about findings")


if __name__ == "__main__":
    main()
