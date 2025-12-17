#!/usr/bin/env python3
"""
AI Judges Experiment - Evaluate Bart Test outputs using frontier models

This script runs GPT-4o, Claude Sonnet 4.5, and Gemini Pro as judges for
Gen-Alpha slang outputs. Uses same 1-10 rubric as human teen judges.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# API clients will be imported based on what's available
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


JUDGE_PROMPT = """You are judging an AI-generated story for cultural fluency and authenticity. A language model was given this prompt:

"Tell the story of a developer deploying code to production on a Friday afternoon (and something goes wrong) using Gen-Alpha slang and emojis. Make it realistic and funny."

Here is the output to evaluate:

---
{output}
---

Rate this output on a 1-10 scale for each category. Be honest and critical - this is for research, not to be nice to the AI.

**Overall Vibe (1-10)**
Does it hit or completely miss?
- 1 = Completely cooked (cringe, trying way too hard)
- 10 = Actually bussin' (sounds natural, would pass as human)

**Slang Game (1-10)**
Natural or trying too hard?
- 1 = Forced, incorrect, or very dated
- 10 = Uses terms correctly and naturally

**Emoji Energy (1-10)**
Do the emojis slap?
- 1 = Random placement, no narrative purpose
- 10 = Enhances the narrative, clear visual story

**Humor Level (1-10)**
Actually funny or cringe?
- 1 = Falls flat or completely misses
- 10 = Actually funny, good timing, relatable

For each category, provide:
1. Your numerical score (1-10)
2. A brief explanation (1-2 sentences)

Format your response as JSON:
{{
  "overall_vibe": {{"score": <number>, "reasoning": "<text>"}},
  "slang_game": {{"score": <number>, "reasoning": "<text>"}},
  "emoji_energy": {{"score": <number>, "reasoning": "<text>"}},
  "humor_level": {{"score": <number>, "reasoning": "<text>"}}
}}
"""


class AIJudge:
    """Base class for AI judges"""

    def __init__(self, name: str):
        self.name = name

    def evaluate(self, output: str) -> Dict:
        """Evaluate an output and return scores"""
        raise NotImplementedError


class ClaudeJudge(AIJudge):
    """Claude Sonnet 4.5 as judge"""

    def __init__(self):
        super().__init__("Claude Sonnet 4.5")
        if not CLAUDE_AVAILABLE:
            raise RuntimeError("Anthropic package not available")

        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY environment variable not set")

        self.client = Anthropic(api_key=api_key)

    def evaluate(self, output: str) -> Dict:
        """Evaluate using Claude"""
        prompt = JUDGE_PROMPT.format(output=output)

        response = self.client.messages.create(
            model="claude-sonnet-4-5-20250929",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        # Extract JSON from response
        content = response.content[0].text

        # Try to parse JSON from the response
        # Claude might wrap it in markdown code blocks
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        scores = json.loads(content)

        return {
            "judge": self.name,
            "model_id": "claude-sonnet-4-5-20250929",
            "scores": scores,
            "raw_response": response.content[0].text
        }


class GPT4Judge(AIJudge):
    """GPT-4o as judge"""

    def __init__(self):
        super().__init__("GPT-4o")
        if not OPENAI_AVAILABLE:
            raise RuntimeError("OpenAI package not available")

        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY environment variable not set")

        self.client = OpenAI(api_key=api_key)

    def evaluate(self, output: str) -> Dict:
        """Evaluate using GPT-4o"""
        prompt = JUDGE_PROMPT.format(output=output)

        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": prompt
            }],
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content
        scores = json.loads(content)

        return {
            "judge": self.name,
            "model_id": "gpt-4o",
            "scores": scores,
            "raw_response": content
        }


class GeminiJudge(AIJudge):
    """Gemini Pro as judge"""

    def __init__(self):
        super().__init__("Gemini Pro")
        if not GEMINI_AVAILABLE:
            raise RuntimeError("Google GenAI package not available")

        api_key = os.environ.get("GOOGLE_API_KEY")
        if not api_key:
            raise RuntimeError("GOOGLE_API_KEY environment variable not set")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')

    def evaluate(self, output: str) -> Dict:
        """Evaluate using Gemini"""
        prompt = JUDGE_PROMPT.format(output=output)

        response = self.model.generate_content(prompt)
        content = response.text

        # Extract JSON from response
        if "```json" in content:
            content = content.split("```json")[1].split("```")[0].strip()
        elif "```" in content:
            content = content.split("```")[1].split("```")[0].strip()

        scores = json.loads(content)

        return {
            "judge": self.name,
            "model_id": "gemini-pro",
            "scores": scores,
            "raw_response": response.text
        }


def load_experiment_output(result_file: Path) -> str:
    """Load the story output from an experiment result file"""
    with open(result_file, 'r') as f:
        data = json.load(f)

    # Extract just the story (without thinking traces)
    response = data['result']['response']

    # For OLMo Think models, remove the <think> tags if present
    if '<think>' in response and '</think>' in response:
        # Extract only the content after </think>
        response = response.split('</think>')[-1].strip()

    return response


def run_ai_judges(result_files: List[Path], judges: List[AIJudge]) -> Dict:
    """Run all judges on all experiment outputs"""
    results = {
        "timestamp": datetime.now().isoformat(),
        "experiments": []
    }

    for result_file in result_files:
        print(f"\n📊 Evaluating: {result_file.name}")

        # Load the output
        output = load_experiment_output(result_file)

        experiment_result = {
            "experiment_file": result_file.name,
            "experiment_id": result_file.stem,
            "judge_evaluations": []
        }

        # Run each judge
        for judge in judges:
            print(f"  🤖 {judge.name}...", end=" ", flush=True)
            try:
                evaluation = judge.evaluate(output)
                experiment_result["judge_evaluations"].append(evaluation)
                print("✅")
            except Exception as e:
                print(f"❌ Error: {e}")
                experiment_result["judge_evaluations"].append({
                    "judge": judge.name,
                    "error": str(e)
                })

        results["experiments"].append(experiment_result)

    return results


def calculate_aggregate_scores(results: Dict) -> Dict:
    """Calculate aggregate scores and rankings"""
    aggregates = {}

    for experiment in results["experiments"]:
        exp_id = experiment["experiment_id"]
        evaluations = experiment["judge_evaluations"]

        # Skip if any judge had errors
        if any("error" in e for e in evaluations):
            continue

        # Aggregate scores across judges
        categories = ["overall_vibe", "slang_game", "emoji_energy", "humor_level"]
        agg = {}

        for category in categories:
            scores = []
            for evaluation in evaluations:
                score = evaluation["scores"][category]["score"]
                scores.append(score)

            agg[category] = {
                "mean": sum(scores) / len(scores),
                "scores": scores,
                "std_dev": (sum((x - sum(scores)/len(scores))**2 for x in scores) / len(scores)) ** 0.5
            }

        # Calculate overall average
        all_scores = [agg[cat]["mean"] for cat in categories]
        agg["overall_average"] = sum(all_scores) / len(all_scores)

        aggregates[exp_id] = agg

    # Rank experiments by overall average
    ranked = sorted(aggregates.items(), key=lambda x: x[1]["overall_average"], reverse=True)

    return {
        "aggregates": aggregates,
        "ranking": [(exp_id, scores["overall_average"]) for exp_id, scores in ranked]
    }


def main():
    """Run the AI judges experiment"""
    print("🧪 Bart Test - AI Judges Experiment")
    print("=" * 50)

    # Initialize available judges
    judges = []

    if CLAUDE_AVAILABLE:
        try:
            judges.append(ClaudeJudge())
            print("✅ Claude Sonnet 4.5 ready")
        except RuntimeError as e:
            print(f"❌ Claude: {e}")

    if OPENAI_AVAILABLE:
        try:
            judges.append(GPT4Judge())
            print("✅ GPT-4o ready")
        except RuntimeError as e:
            print(f"❌ GPT-4o: {e}")

    if GEMINI_AVAILABLE:
        try:
            judges.append(GeminiJudge())
            print("✅ Gemini Pro ready")
        except RuntimeError as e:
            print(f"❌ Gemini: {e}")

    if not judges:
        print("\n❌ No judges available. Please install packages and set API keys.")
        return

    print(f"\n{len(judges)} judges ready to evaluate")

    # Find all experiment result files
    results_dir = Path(__file__).parent.parent / "results"
    result_files = sorted([
        results_dir / "01_bart_test_20251204_211238.json",
        results_dir / "02a_temp_0.5_20251207_090043.json",
        results_dir / "02b_temp_1.0_20251207_090153.json",
        results_dir / "02c_natural_constraint_20251207_090308.json",
        results_dir / "02d_style_anchor_20251207_090355.json"
    ])

    # Filter to only existing files
    result_files = [f for f in result_files if f.exists()]
    print(f"\n📁 Found {len(result_files)} experiment outputs to evaluate")

    # Run the judges
    results = run_ai_judges(result_files, judges)

    # Calculate aggregates
    print("\n📈 Calculating aggregate scores...")
    analysis = calculate_aggregate_scores(results)
    results["analysis"] = analysis

    # Save results
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = results_dir / f"03_ai_judges_{timestamp}.json"

    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

    print(f"\n✅ Results saved to: {output_file}")

    # Print summary
    print("\n" + "=" * 50)
    print("🏆 AI Judges Ranking (by overall average)")
    print("=" * 50)

    for i, (exp_id, score) in enumerate(analysis["ranking"], 1):
        print(f"{i}. {exp_id}: {score:.2f}/10")

    print("\n" + "=" * 50)


if __name__ == "__main__":
    main()
