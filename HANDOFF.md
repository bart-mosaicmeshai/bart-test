# Bart Test - Session Handoff

**Date**: December 7, 2024
**Current Status**: Experiment 02 complete, awaiting teen judge reviews

---

## Project Context

The **Bart Test** is a signature LLM benchmark that evaluates models using Gen-Alpha slang, emojis, and technical storytelling. It's rated by actual teenagers, not automated metrics.

**The Test**: "Tell the story of a developer deploying code to production on a Friday afternoon (and something goes wrong) using Gen-Alpha slang and emojis. Make it realistic and funny."

**Purpose**:
- Measure LLM cultural fluency (something traditional benchmarks miss)
- Create ongoing series testing every new model release
- Build authority as "the Bart Test guy"
- Document how AI handles natural language evolution

---

## What We Just Completed (Dec 7, 2024)

### Experiment 02: Constraint Experiments
Testing the "overthinking" hypothesis with 4 variations on OLMo 3 32B Think:

1. **02a - Lower Temp (0.5)**: 1,216 tokens (+15%) - still overthinks
2. **02b - Higher Temp (1.0)**: 1,585 tokens (+50%) - MORE overthinking!
3. **02c - Natural Constraint** ("max 5 slang terms"): 1,707 tokens (+61%) - AI ignored constraint
4. **02d - Style Anchor** ("texting a friend"): 1,044 tokens (-1.5%) - ⭐ best result

**Key Findings**:
- Temperature tuning doesn't fix reasoning model overthinking
- Explicit constraints backfire (Goodhart's Law)
- Social context framing shows most promise
- Prompt framing > sampling parameters

### Documentation Updates
- ✅ Updated README.md with Experiment 02 results and findings
- ✅ Updated prompts/bart_test.md with detailed methodology
- ✅ Added AI judges framework (GPT-4o, Claude, Gemini as evaluators)
- ✅ Created review template CSV for Google Sheets workflow
- ✅ Updated blog series outline (ongoing series structure)
- ✅ Drafted blog post #2: "Finding the Sweet Spot"
- ✅ Created presentation ideas doc (gitignored)

### Files in Repo
```
experiments/
├── 01_bart_test.py              # OLMo baseline
└── 02_constraint_experiments.py # 4 variations runner

results/
├── 01_bart_test_20251204_211238.json      # Baseline (1,060 tokens)
├── 02a_temp_0.5_20251207_090043.json      # Lower temp
├── 02b_temp_1.0_20251207_090153.json      # Higher temp
├── 02c_natural_constraint_20251207_090308.json  # Constraint
├── 02d_style_anchor_20251207_090355.json   # Style anchor ⭐
└── bart_test_review_template.csv          # Judge review template

blog-drafts/ (gitignored)
├── 01-introducing-the-bart-test.md  # Post 1 (draft complete)
├── 02-finding-the-sweet-spot.md     # Post 2 (draft complete)
├── SERIES-OUTLINE.md                 # Full series plan
└── PRESENTATION-IDEAS.md             # Conference talk notes
```

---

## Current State

### Waiting On
- **Teen judge reviews** of all 5 experiments (baseline + 4 variations)
- Google Sheet: "LLM Test Reviews 2025-12-07"
- Multiple judges rating on 1-10 scale (Overall Vibe, Slang Game, Emoji Energy, Humor Level)

### Blog Series Status
- **Launch Arc** (Parts 1-3): Introducing Bart Test + OLMo results
  - Part 1: Draft complete ✅
  - Part 2: Draft complete ✅ (awaiting judge data)
  - Part 3: Planned (full judge analysis)
  - Part 4: Planned (AI judges experiment)
- **Ongoing Series**: Individual model reviews as released
- **Backtest Series**: Testing existing models (GPT-4o, Claude, Llama, etc.)
- **Quarterly Roundups**: Meta-analysis and leaderboards

### Publication Schedule
- Dec 15: Part 1 (Introducing the Bart Test)
- Dec 22: Part 2 (Finding the Sweet Spot + judge results)
- Dec 29: Part 3 (What the Teen Judges Said)
- Jan 2025+: Backtest series (1-2 models/week)

---

## Next Steps / Potential Tasks

### Immediate (Waiting on Teen Judges)
1. **Collect judge reviews** from Google Sheet
2. **Analyze results** - Which experiment won? Inter-rater reliability?
3. **Update blog post #2** with actual judge data
4. **Write blog post #3** - Full judge analysis

### AI Judges Experiment (Part 4)
1. **Create API client scripts** for GPT-4o, Claude Sonnet 4.5, Gemini Pro
2. **Design judge prompt** - Same 1-10 rubric as humans
3. **Run all 5 experiments through AI judges** (blind evaluation)
4. **Analyze agreement** - Where do human/AI judges align/disagree?
5. **Write blog post #4** - "When AI Judges AI Slang"

### Backtest Series (Building Leaderboard)
Priority order for testing:
1. **GPT-4o** (OpenAI API)
2. **Claude 3.5 Sonnet** (Anthropic API)
3. **Llama 3.1 8B Instruct** (local via LM Studio)
4. **Gemini Pro** (Google API)
5. **Qwen 2.5 32B** (local via LM Studio)

For each model:
- Run Bart Test (baseline + style anchor approach)
- Get teen judge reviews
- Get AI judge reviews
- Publish individual model post
- Update leaderboard

### Analysis & Tools
1. **Aggregation script** - Analyze Google Sheets judge data
2. **Leaderboard generator** - Auto-update from results
3. **Inter-rater reliability** - Calculate Krippendorff's alpha
4. **Visualization scripts** - Generate charts for blog posts

### Presentation Development
- Build slide deck from PRESENTATION-IDEAS.md
- Record demo video of running the test
- Submit to conferences (PyCon, PyData, etc.)
- Start with local meetup lightning talks

---

## Important Context for Next Agent

### Design Decisions Made
1. **1-10 scale for all ratings** (not 1-5) - less mental load for reviewers
2. **Social framing > constraints** - "texting a friend" works better than explicit limits
3. **AI judges are experimental** - Human teens remain ground truth
4. **Ongoing series structure** - Not a finite 6-part series, continuous testing
5. **Blog posts in blog-drafts/** - Gitignored until ready to publish

### Key Insights to Remember
- **"ELA project" effect**: AI treats creative tasks like homework assignments
- **Goodhart's Law in action**: Explicit constraints make overthinking worse
- **Token count as proxy**: Correlates with "trying too hard" vibes
- **Visible thinking traces**: OLMo 3 Think literally lists slang terms before using them

### Files to Keep Private (Gitignored)
- `blog-drafts/` - All drafts until published
- Teen judge identities - Always anonymized as "Judge #1", "Judge #2", etc.
- Personal notes in PRESENTATION-IDEAS.md

### Technical Setup
- **Hardware**: Apple M4 Max, 128GB RAM
- **Local models**: LM Studio (http://localhost:1234)
- **Python**: venv at `./venv/`
- **Model tested**: OLMo 3 32B Think (Q4_K_M quantization)

---

## Quick Start Commands

```bash
# Activate venv
source venv/bin/activate

# Run baseline test
python experiments/01_bart_test.py

# Run constraint experiments (all 4 variations)
python experiments/02_constraint_experiments.py

# Check git status
git status

# View recent commits
git log --oneline -5
```

---

## Questions for User / Clarifications Needed

When resuming, check with user:
1. Have teen judge reviews come in yet?
2. Ready to start AI judges experiment?
3. Which model should we test next for backtest series?
4. Any adjustments needed to methodology based on judge feedback?

---

## Resources & Links

- **GitHub Repo**: https://github.com/bart-mosaicmeshai/bart-test
- **Blog**: https://www.mosaicmeshai.com/blog
- **Inspiration**: [Simon Willison's OLMo 3 post](https://simonwillison.net/2025/Nov/22/olmo-3/)
- **Google Sheet**: "LLM Test Reviews 2025-12-07" (user has access)

---

**Last Updated**: December 7, 2024
**Next Session**: Analyze teen judge results or start AI judges experiment
