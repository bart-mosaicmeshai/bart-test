# AI Judges - Hybrid Evaluation System

This system uses AI judges (GPT-4o, Claude, Gemini) for pre-screening, then gets final validation from human teen judges. Best of both worlds: speed + authenticity.

## The Workflow

```
┌─────────────────┐
│ New LLM Output  │
└────────┬────────┘
         │
         v
┌─────────────────┐
│ AI Judges       │  ← GPT-4o, Claude, Gemini
│ Score 1-10      │     (Same rubric as humans)
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Top 2 Finalists │  ← Automated ranking
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Teen A/B Review │  ← Your kids: 5 min, simple choice
└────────┬────────┘
         │
         v
┌─────────────────┐
│ Final Verdict   │  ← Human ground truth wins
└─────────────────┘
```

## Setup

### 1. Install Dependencies

```bash
# Activate your venv
source venv/bin/activate

# Install API packages
pip install -r requirements.txt
```

### 2. Set API Keys

You need at least one of these (all three is best):

```bash
# Add to your ~/.bashrc or ~/.zshrc:
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
export GOOGLE_API_KEY="..."
```

Or create a `.env` file (gitignored):

```bash
# .env
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
GOOGLE_API_KEY=...
```

### 3. Get API Keys

**Claude (Anthropic)**: https://console.anthropic.com/
- Create account → Settings → API Keys
- ~$3-5 per experiment (cheap)

**GPT-4o (OpenAI)**: https://platform.openai.com/
- Create account → API Keys
- ~$0.15-0.30 per experiment (very cheap)

**Gemini (Google)**: https://aistudio.google.com/app/apikey
- Sign in with Google → Get API key
- Free tier available!

## Usage

### Step 1: Run AI Judges

This evaluates all 5 Experiment 02 outputs:

```bash
python experiments/03_ai_judges.py
```

**Output:**
- `results/03_ai_judges_TIMESTAMP.json` - Full results with scores
- Console shows ranking by overall average

**Time:** ~2-3 minutes (depending on API speed)

### Step 2: Generate Teen Review Sheets

Creates simplified comparison for your kids:

```bash
python experiments/04_teen_review_generator.py
```

**Output:**
- `results/teen_review_top2_comparison.md` - A vs B comparison (5 min)
- `results/teen_review_full_ranking.md` - All 5 if they want (10 min)

### Step 3: Get Human Reviews

Share the markdown files with your kids:

1. Open `teen_review_top2_comparison.md`
2. They read 2 stories, pick which feels more natural
3. Takes ~5 minutes

**Pro tip:** Frame it as "help me validate my AI experiment" - they get to fact-check AI!

### Step 4: Analyze Agreement

After collecting human reviews:

```bash
python experiments/05_combined_analysis.py
```

**Output:**
- `results/combined_analysis.json` - Full comparison
- Shows where AI/human judges agree or disagree

## What You're Testing

### Research Questions

1. **Can AI judges identify "natural" vs "forced" slang?**
2. **Where do AI and human judges agree/disagree?**
3. **Is correlation strong enough (>0.7) to trust AI pre-screening?**

### If Correlation is Strong

✅ Use AI judges as primary evaluators going forward
✅ Spot-check with teens quarterly (1-2 samples)
✅ Ship blog posts within hours of testing new models

### If Correlation is Weak

❌ AI judges miss the mark on authenticity
⚠️ Fall back to your own expert analysis
📝 Write about why AI can't judge cultural fluency (great content!)

## The Teen Review Strategy

### Keep It Lightweight

**Good:**
- "Which one sounds more like a real person?"
- Quick A/B choice
- Optional comment box
- 5 minutes max

**Bad:**
- "Rate these 5 things on a 10-point scale"
- Long written explanations required
- Feels like homework

### Keep Them Engaged

**Frame it right:**
- "Help me test if AI can judge other AI"
- "You're the ground truth"
- Show them the AI scores after (make it interesting)

**Respect their time:**
- Max 1-2 reviews per week
- Bundle multiple tests into one session
- Always thank them (pizza helps)

## Files Created

```
experiments/
├── 03_ai_judges.py              # Main judge runner
├── 04_teen_review_generator.py  # Create comparison sheets
└── 05_combined_analysis.py      # Merge AI + human scores

results/
├── 03_ai_judges_*.json          # AI judge outputs
├── teen_review_top2_comparison.md   # A/B comparison
├── teen_review_full_ranking.md      # Full ranking (optional)
└── combined_analysis.json           # Final analysis
```

## Costs

Estimated per full evaluation (5 outputs × 3 judges):

- **GPT-4o**: ~$0.15 (input) + $0.15 (output) = $0.30
- **Claude**: ~$3 (input) + $1 (output) = $4
- **Gemini**: Free tier (15 RPM) or ~$0.50

**Total per experiment**: ~$5 (mostly Claude)

**For 50 models/year**: ~$250 (very reasonable for a signature benchmark)

## Next Steps

Once you validate the hybrid approach:

1. **Backtest existing models** (GPT-4o, Claude, Llama, Qwen)
2. **Build leaderboard** (auto-updated from results)
3. **Set up alerting** (new model drops → auto-test within 24hrs)
4. **Write blog post #4**: "When AI Judges AI Slang"

## Troubleshooting

**"ANTHROPIC_API_KEY not set"**
→ Add to environment or `.env` file

**"No judges available"**
→ At least one API key must be set

**"Rate limit exceeded"**
→ Wait a minute, or reduce concurrent calls

**"JSON parsing error"**
→ AI judge didn't format response correctly (rare, will auto-retry)

## Example Output

```
🧪 Bart Test - AI Judges Experiment
==================================================
✅ Claude Sonnet 4.5 ready
✅ GPT-4o ready
✅ Gemini Pro ready

3 judges ready to evaluate

📁 Found 5 experiment outputs to evaluate

📊 Evaluating: 01_bart_test_20251204_211238.json
  🤖 Claude Sonnet 4.5... ✅
  🤖 GPT-4o... ✅
  🤖 Gemini Pro... ✅

[... evaluates all 5 experiments ...]

==================================================
🏆 AI Judges Ranking (by overall average)
==================================================
1. 02d_style_anchor_20251207_090355: 7.2/10
2. 01_bart_test_20251204_211238: 6.8/10
3. 02a_temp_0.5_20251207_090043: 6.1/10
4. 02b_temp_1.0_20251207_090153: 5.4/10
5. 02c_natural_constraint_20251207_090308: 4.9/10
```

---

**Questions?** Check the main README or open an issue.
