# The Bart Test

**A signature benchmark for evaluating LLM reasoning through Gen-Alpha slang, emojis, and technical storytelling.**

> "Tell the story of a developer deploying code to production on a Friday afternoon (and something goes wrong) using Gen-Alpha slang and emojis. Make it realistic and funny."

## What is the Bart Test?

The Bart Test is a universal LLM evaluation that combines:
- **Technical understanding** (software deployment, DevOps concepts)
- **Cultural awareness** (current Gen-Alpha slang usage)
- **Creative expression** (emoji storytelling, humor)
- **Human judgment** (rated by actual teenagers, not benchmarks)

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

Human judges (my two teenagers) provide the authoritative rating on a 1-10 scale:
- **1** = Completely cooked (cringe, trying way too hard)
- **10** = Actually bussin' (sounds natural, would pass as human)
- **Context matters**: Does it sound like a teen or an adult wrote it?

## Results

### OLMo 3 32B Think (Q4_K_M)
- **Date**: December 4, 2024
- **Tokens**: 1,060 (extensive thinking traces visible)
- **Duration**: 44 seconds
- **Teen Judge #1**: 4-5/10 - "It's definitely AI... a little bit aggressive with all the slang... Just like… a little too much"
- **Teen Judge #2**: 6/10 (if teen) / 2/10 (if adult) - "Sounds like my ELA project where we had to use as much slang as possible"
- **Key insight**: AI approached it like homework - maximizing slang density instead of being natural
- **Status**: ⭐ First baseline result
- [Full output →](results/01_bart_test_20251204_211238.json)

### Coming Soon
- Llama 3.1 8B Instruct
- GPT-4o
- Claude 3.5 Sonnet
- Gemini Pro
- Future models as they're released

## Project Structure

```
bart-test/
├── README.md
├── experiments/           # Test scripts for different models
│   └── 01_bart_test.py   # OLMo 3 baseline
├── prompts/
│   └── bart_test.md      # Full test documentation & rubric
├── results/              # JSON outputs from each test
├── scripts/
│   └── olmo_client.py    # LM Studio API client
└── blog-drafts/          # Blog post drafts (gitignored)
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
python experiments/01_bart_test.py
```

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
