# The Bart Test

**A benchmark for evaluating LLM cultural fluency through Gen-Alpha slang and emojis, rated by actual teenagers.**

> **Project Status (January 2025):** This project is **paused**. After 5 experiments and multiple methodology iterations, I've documented key learnings about LLM cultural fluency evaluation, human evaluation design, and research methodology. The complete journey—including what worked, what didn't, and why I'm pausing—is captured in a [10-part blog series](https://www.mosaicmeshai.com/blog/bart-test-part-10-the-stochastic-parrot-and-what-visible-thinking-traces-might-reveal) published at Mosaic Mesh AI.

---

## What Was the Bart Test?

The Bart Test explored whether LLMs could generate natural Gen-Alpha slang and emojis, as judged by actual teenagers. Through 5 experiments across late 2024 and early 2025, the project tested multiple models, iterated on methodology, and discovered insights about:

- How reasoning models "overthink" creative tasks
- What makes AI-generated slang feel "forced" or "trying too hard"
- The challenges of designing sustainable human evaluation systems
- The social costs of recruiting teenage judges
- When "interesting research" doesn't translate to "useful tool"

## Read the Full Story

The 10-part blog series documents the complete journey:

1. **[Part 1: When AI Does Its Homework Too Well](https://www.mosaicmeshai.com/blog/bart-test-part-1-when-ai-does-its-homework-too-well)** - Initial OLMo experiment, teen feedback
2. **[Part 2: Testing the Overthinking Hypothesis](https://www.mosaicmeshai.com/blog/bart-test-part-2-testing-the-overthinking-hypothesis)** - Constraint experiments
3. **[Part 3: The Zoo-Not-Duck Problem](https://www.mosaicmeshai.com/blog/bart-test-part-3-the-zoo-not-duck-problem)** - Teen insights on "trying too hard"
4. **[Part 4: When My Teen Judges Ghosted Me](https://www.mosaicmeshai.com/blog/bart-test-part-4-when-my-teen-judges-ghosted-me)** - First methodology failure
5. **[Part 5: Redesigning From Scratch](https://www.mosaicmeshai.com/blog/bart-test-part-5-redesigning-from-scratch)** - The pivot to paper sheets and batch judging
6. **[Part 6: The American Ninja Warrior Problem](https://www.mosaicmeshai.com/blog/bart-test-part-6-the-american-ninja-warrior-problem)** - Test design philosophy
7. **[Part 7: The Social Cost I Didn't See Coming](https://www.mosaicmeshai.com/blog/bart-test-part-7-the-social-cost-i-didnt-see-coming)** - Judge recruitment challenges
8. **[Part 8: When an Interesting Experiment Might Not Be a Useful Tool](https://www.mosaicmeshai.com/blog/bart-test-part-8-when-an-interesting-experiment-might-not-be-a-useful-tool)** - Questioning value proposition
9. **[Part 9: The Question I Couldn't Answer](https://www.mosaicmeshai.com/blog/bart-test-part-9-the-question-i-couldnt-answer)** - Final results and insufficient data
10. **[Part 10: The Stochastic Parrot Question](https://www.mosaicmeshai.com/blog/bart-test-part-10-the-stochastic-parrot-and-what-visible-thinking-traces-might-reveal)** - Deeper reflections on cognition

---

## Key Learnings

### What Worked
- Paper evaluation sheets (reduced friction dramatically)
- Short relatable scenarios vs. long technical stories
- Batch judging approach (quarterly vs. per-model)
- Documenting the journey publicly
- Getting honest teen feedback on AI outputs
- Testing local models (OLMo, Llama, Qwen) to see thinking traces

### What Didn't Work
- Per-model validation (doesn't scale)
- Text message-based evaluation (too clunky)
- Long technical deployment scenarios (too specialized)
- Assuming free judges stay motivated
- Building methodology before validating utility

### Key Insights About LLMs
- Reasoning models visibly "overthink" creative tasks with explicit planning
- "Trying too hard" with slang is quantifiable and reproducible
- Social framing ("texting a friend") affects output more than temperature tuning
- Length signals inauthenticity (26 words = natural, 50+ words = forced)
- Cultural fluency has a half-life (slang dates quickly)

### Methodology Insights
- Human evaluation requires respect for judge time and social costs
- Interesting research doesn't always equal useful tool
- Design around constraints rather than fighting them
- Ask "so what?" earlier in exploratory work
- When measurement complexity exceeds insight value, pause and reflect

## Experiments Conducted

The project ran 5 experiments with multiple models:

- **Experiment 01**: OLMo 3 32B Think baseline - Discovered "overthinking" and "ELA project" effect
- **Experiment 02**: Constraint experiments (temperature, explicit limits, social framing) - Style framing worked best
- **Experiment 03**: Hybrid AI/human evaluation - AI judges aligned with human judges, but teen judges ghosted
- **Experiment 04**: New methodology with paper sheets, short scenarios - Process validated, revealed length/emoji density issues
- **Experiment 05**: Refined prompts with tighter constraints - Insufficient judge data to draw conclusions

Models tested: OLMo 3 32B Think, Llama 3.1 8B, Qwen3 14B, GPT-5.2, Claude Opus 4.5, Gemini 3 Pro (blocked by safety filters)

All experiment outputs, evaluation sheets, and detailed analysis are preserved in the repository for anyone interested in continuing this work.

## Project Structure

```
bart-test/
├── README.md
├── HANDOFF.md                      # Project status and decision log
├── PROCESS.md                      # Complete evaluation workflow
├── experiments/                    # Test scripts for all 5 experiments
│   ├── 01_bart_test.py            # OLMo 3 baseline
│   ├── 02_constraint_experiments.py # Temperature & prompt variations
│   ├── 03_ai_judges.py            # Hybrid AI/human evaluation
│   ├── 04_new_prompts_test_*.py   # New methodology (frontier, llama, qwen, olmo)
│   └── 05_new_prompts_test_*.py   # Refined prompts (frontier, llama, qwen, olmo)
├── prompts/
│   └── bart_test.md               # Original test documentation & rubric
├── results/                       # JSON outputs from all experiments
│   ├── 01_experiment_runs/        # OLMo baseline
│   ├── 02_experiment_runs/        # Constraint variations
│   ├── 03_experiment_runs/        # Frontier models + AI judges
│   ├── 04_final_outputs/          # Experiment 04 validated outputs
│   └── 05_final_outputs/          # Experiment 05 outputs (not fully validated)
├── evaluation_sheets/             # Paper evaluation sheets and ratings
│   ├── 20251228/                  # Experiment 04 evaluation
│   └── 20251230/                  # Experiment 05 evaluation
└── scripts/
    └── olmo_client.py             # LM Studio API client
```

## For Anyone Continuing This Work

All scripts, prompts, evaluation sheets, and methodology documentation are preserved in this repository. Key files:

- **[PROCESS.md](PROCESS.md)** - Complete step-by-step workflow for running evaluations
- **[HANDOFF.md](HANDOFF.md)** - Full project history, decisions, and learnings
- **[prompts/bart_test.md](prompts/bart_test.md)** - Test specifications and rubrics
- **evaluation_sheets/** - HTML templates and completed ratings

The methodology evolved significantly through 5 experiments. Read HANDOFF.md for the complete context before continuing.

## Inspiration & Resources

This project was inspired by:
- **Simon Willison's** [OLMo 3 analysis](https://simonwillison.net/2025/Nov/22/olmo-3/) on overthinking
- **Allen AI's** open approach with OLMo 3 and Dolma 3
- My teenagers, who provided honest feedback about what actually sounds natural

---

## License

MIT

---

**Read the full story**: [10-Part Blog Series at Mosaic Mesh AI](https://www.mosaicmeshai.com/blog/bart-test-part-10-the-stochastic-parrot-and-what-visible-thinking-traces-might-reveal)
