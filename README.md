# The Bart Test

**A signature benchmark for evaluating LLM cultural fluency through Gen-Alpha slang and emojis, rated by actual teenagers.**

> **Note (January 2025):** The Bart Test methodology is being redesigned based on learnings from initial experiments. This README describes the original approach. See the [blog series](https://www.mosaicmeshai.com/blog) (launching Jan 7, 2025) for the full story of the pivot and new validation approach.

**Original prompt:**
> "Tell the story of a developer deploying code to production on a Friday afternoon (and something goes wrong) using Gen-Alpha slang and emojis. Make it realistic and funny."

## What is the Bart Test?

The Bart Test is a universal LLM evaluation that combines:
- **Technical understanding** (software deployment, DevOps concepts)
- **Cultural awareness** (current Gen-Alpha slang usage)
- **Creative expression** (emoji storytelling, humor)
- **Human judgment** (rated by actual teenagers, not benchmarks)
- **AI judges** (experimental: frontier models evaluating cultural fluency)

Unlike traditional benchmarks, the Bart Test reveals whether models **overthink** simple creative tasks and whether their outputs sound natural or forced.

## Why This Test Matters

Inspired by Simon Willison's [discovery](https://simonwillison.net/2025/Nov/22/olmo-3/) that OLMo 3 spent 14+ minutes generating 8,437 tokens for a simple SVG task, the Bart Test measures:

1. **Overthinking** - Do models spend excessive tokens planning creative tasks?
2. **Cultural fluency** - Can models use current slang naturally without being "cringe"?
3. **Natural expression** - Do outputs feel human or artificially dense?
4. **Human-AI alignment** - What do real teenagers think of AI-generated slang?

The test also serves a bonus purpose: **teaching me Gen-Alpha slang** so I can be appropriately cringe around my kids. 😄

## Scoring Rubric

Total: 25 points

- **Slang Accuracy** (5 pts) - Uses current terms correctly and naturally
- **Emoji Storytelling** (5 pts) - Visual narrative enhances the story
- **Technical Accuracy** (5 pts) - Realistic deployment scenario
- **Humor** (5 pts) - Actually funny, good timing, relatable
- **Coherence** (5 pts) - Clear story arc, flows well

**Human judges** (my two teenagers + friends) provide the authoritative rating on a 1-10 scale:
- **Overall Vibe**: Does it hit or completely miss?
- **Slang Game**: Natural or trying too hard?
- **Emoji Energy**: Do the emojis slap?
- **Humor Level**: Actually funny or cringe?

**AI judges** (experimental - GPT-4o, Claude Sonnet 4.5, Gemini Pro):
- Same 1-10 rubric as human judges
- Tests whether frontier models can identify "forced" vs "natural" slang
- Validates human ratings and enables rapid model testing
- Tracks judge correlation: Are AI judges getting better at cultural fluency?

## Results

### Experiment 01: OLMo 3 32B Think Baseline (Q4_K_M)
- **Date**: December 4, 2024
- **Tokens**: 1,060 (extensive thinking traces visible)
- **Duration**: 44 seconds
- **Temperature**: 0.7
- **Teen Judge #1**: 4-5/10 - "It's definitely AI... a little bit aggressive with all the slang... Just like… a little too much"
- **Teen Judge #2**: 6/10 (if teen) / 2/10 (if adult) - "Sounds like my ELA project where we had to use as much slang as possible"
- **Key insight**: AI approached it like homework - maximizing slang density instead of being natural
- **Status**: ⭐ First baseline result
- [Full output →](results/01_bart_test_20251204_211238.json)

### Experiment 02: Constraint Experiments (December 7, 2024)

Testing the "overthinking" hypothesis with 4 variations on OLMo 3 32B Think:

| Experiment | Description | Tokens | Duration | Status |
|------------|-------------|--------|----------|--------|
| **02a** - Lower Temp (0.5) | Reduce randomness to test if it produces more natural slang | 1,216 | 50.7s | Still overthinks |
| **02b** - Higher Temp (1.0) | Increase randomness for more natural variation | 1,585 | 67.3s | MORE overthinking! |
| **02c** - Natural Constraint | Explicitly limit to max 5 slang terms | 1,707 | 71.7s | AI ignored constraint |
| **02d** - Style Anchor | "Write like texting a friend who codes" framing | 1,044 | 43.8s | ⭐ Shortest/fastest |

**Key Findings:**
- Temperature changes didn't help - higher temp made it worse
- Explicit constraints backfired - AI overthought even more trying to follow them
- **Style anchoring** (social context framing) showed most promise - closest to baseline length
- Results suggest prompt framing matters more than temperature tuning for this model

**Status**: Awaiting teen judge evaluations (in progress)

[Full outputs →](results/)

### Coming Soon
- Analysis of teen judge ratings from Experiment 02
- Llama 3.1 8B Instruct
- GPT-4o
- Claude 3.5 Sonnet
- Gemini Pro
- Future models as they're released

## Project Structure

```
bart-test/
├── README.md
├── experiments/                    # Test scripts for different models
│   ├── 01_bart_test.py            # OLMo 3 baseline
│   └── 02_constraint_experiments.py # Temperature & prompt variations
├── prompts/
│   └── bart_test.md               # Full test documentation & rubric
├── results/                       # JSON outputs from each test
│   ├── 01_bart_test_*.json       # Baseline results
│   ├── 02a_temp_0.5_*.json       # Lower temperature
│   ├── 02b_temp_1.0_*.json       # Higher temperature
│   ├── 02c_natural_constraint_*.json # Max 5 slang constraint
│   ├── 02d_style_anchor_*.json   # Texting friend framing
│   └── bart_test_review_template.csv # Review template for judges
├── scripts/
│   └── olmo_client.py            # LM Studio API client
└── blog-drafts/                  # Blog post drafts (gitignored)
```

## Running the Test

### Setup

```bash
# Clone the repo
git clone https://github.com/bart-mosaicmeshai/bart-test.git
cd bart-test

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### For Local Models (LM Studio)

1. Load your model in LM Studio
2. Start the local API server (default: `http://localhost:1234`)
3. Run the test:

```bash
# Run baseline test
python experiments/01_bart_test.py

# Run constraint experiments (4 variations)
python experiments/02_constraint_experiments.py
```

### Analyzing Results

After running experiments, share results with teen judges:

1. Import `results/bart_test_review_template.csv` to Google Sheets
2. Hide columns A & B (experiment metadata)
3. Duplicate sheet for each judge
4. Judges rate on 1-10 scale:
   - Overall Vibe
   - Slang Game (natural vs. trying too hard)
   - Emoji Energy
   - Humor Level

### For API Models

Coming soon: Scripts for OpenAI, Anthropic, Google APIs

## The Vision

Every time a new model drops, I run the Bart Test and document the results in my [blog series](https://www.mosaicmeshai.com/blog). Over time, this creates:

- A growing dataset of model comparisons
- Documentation of how AI improves at natural language
- A record of slang evolution across months/years
- Authority as "the Bart Test guy"
- Easy, repeatable content for my blog
- A crash course in Gen-Alpha slang for myself

## Inspiration

- **Simon Willison's** [OLMo 3 analysis](https://simonwillison.net/2025/Nov/22/olmo-3/) on overthinking
- **Allen AI's** open approach with OLMo 3 and Dolma 3
- My teenagers, who keep me honest about what's actually "bussin'"

## Resources

### OLMo 3 Specific
- [Model Card (Hugging Face)](https://huggingface.co/allenai/Olmo-3-32B-Think)
- [OLMo 3 Blog Post](https://allenai.org/blog/olmo3)
- [LM Studio Model Page](https://lmstudio.ai/models/allenai/olmo-3-32b-think)
- [GGUF Quantizations](https://huggingface.co/lmstudio-community/Olmo-3-32B-Think-GGUF)
- [Dolma 3 Training Data](https://huggingface.co/datasets/allenai/dolma)
- [OlmoTrace Tool](https://olmotrace.allenai.org/)

### General
- [LM Studio](https://lmstudio.ai/) - Local LLM inference
- [Simon Willison's Blog](https://simonwillison.net/) - LLM research and analysis

## Contributing

Want to run the Bart Test on a model I haven't tested yet? PRs welcome! Please include:
- Model name and version
- Inference setup (local/API, quantization if applicable)
- Raw JSON output
- Your own human evaluation (bonus points if rated by actual teenagers)

## License

MIT

---

**Follow the series**: [Mosaic Mesh AI Blog](https://www.mosaicmeshai.com/blog)

**Connect**: [GitHub](https://github.com/bart-mosaicmeshai) | [Twitter/X](#) | [LinkedIn](#)
