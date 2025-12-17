# Quick Start: AI Judges System

**TL;DR**: Hybrid evaluation system that uses AI for speed + your kids for validation.

## The 3-Step Process

### Step 1: Run AI Judges (~3 minutes)

```bash
# Set API keys first
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
export GOOGLE_API_KEY="..."

# Run judges
python experiments/03_ai_judges.py
```

**Output:** Ranked list of all 5 experiments (1-10 scores)

### Step 2: Generate Teen Reviews (~30 seconds)

```bash
python experiments/04_teen_review_generator.py
```

**Output:**
- `results/teen_review_top2_comparison.md` - Show this to your kids

### Step 3: Get Human Validation (~5 minutes)

Share the comparison file with your kids:
- Read 2 stories side-by-side
- Pick which one feels more natural
- Optional: Add quick notes

## What This Tells You

**If AI and humans agree (correlation >0.7):**
✅ Use AI judges for future tests
✅ Spot-check with humans quarterly
✅ Ship blog posts within hours of new model releases

**If they disagree:**
❌ AI misses cultural authenticity
📝 Fall back to your expert analysis
💡 Great content: "Why AI Can't Judge Slang"

## API Key Setup

### Claude (Best for this task)
1. Go to https://console.anthropic.com/
2. Settings → API Keys
3. Cost: ~$4 per full evaluation

### OpenAI (Cheapest)
1. Go to https://platform.openai.com/
2. API Keys
3. Cost: ~$0.30 per full evaluation

### Gemini (Free tier!)
1. Go to https://aistudio.google.com/app/apikey
2. Get API key
3. Cost: Free (15 RPM limit)

## Costs

Per evaluation (5 outputs × 3 judges):
- **Total**: ~$5
- **Annual** (50 models): ~$250

Very reasonable for a signature benchmark!

## Files Created

```
experiments/
├── 03_ai_judges.py              # Main judge runner
├── 04_teen_review_generator.py  # Teen comparison sheets
└── 05_combined_analysis.py      # Agreement analysis

AI_JUDGES_README.md              # Full documentation
```

## Next Steps After Validation

1. Backtest existing models (GPT-4o, Claude, Llama)
2. Build auto-updating leaderboard
3. Set up alerting for new model releases
4. Write blog post: "When AI Judges AI Slang"

## Questions?

See `AI_JUDGES_README.md` for full documentation.
