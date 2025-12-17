# Bart Test - Session Handoff

**Date**: December 17, 2024
**Current Status**: Strategic pivot - Committing to benchmark approach, not prompt engineering

**Next Critical Decision**: Run Experiment 03 to test if prompt causes "trying too hard" problem

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

## Recent Updates

### December 17, 2024: Hybrid Evaluation Complete ✅

**What We Did:**
1. ✅ Ran Claude AI judge on all 5 Experiment 02 outputs
2. ✅ Collected human feedback from 3 teen reviewers via text
3. ✅ Validated hybrid approach (AI pre-screen + human validation)

**AI Judge Results** (Claude Sonnet 4.5):
1. Lower Temp (0.5): 5.25/10
2. Higher Temp (1.0): 5.00/10
3. Baseline / Natural Constraint / Style Anchor: 4.50/10 (tied)

**Human Judge Results** (3 teens, text message reviews):
- **Winner: Lower Temp (0.5)** - 2 out of 3 votes
- Second: Baseline (0.7) - 1 vote

**Key Finding:** ✅ **AI and human judges agree on winner!**

**Core Insights from Teens:**
- ❌ **"Trying too hard" problem**: All stories over-index on slang density
- ❌ **Dated slang**: "no cap" and "vibe" already feel old
- ❌ **Emoji overuse**: Should stick to core set (😂😭🔥🥀)
- ✅ **Natural mixing works**: Blend slang with normal English, don't replace everything
- 📝 **Teen #1 quote**: "It's like painting a zoo when you want a duck - too much noise"

**Files Created:**
- `results/human_reviews_20251217.md` - Complete teen feedback analysis
- `results/03_ai_judges_20251217_130645.json` - AI judge scores

**Validation:** Hybrid approach works! AI judges can pre-screen, humans validate quickly (5-10 min per teen).

---

### December 9, 2024: AI Judges System Built

Built hybrid evaluation system (AI pre-screening + teen validation):

**New Scripts:**
1. **03_ai_judges.py** - Runs GPT-4o, Claude, Gemini as judges
2. **04_teen_review_generator.py** - Creates simple A/B comparisons from AI results
3. **05_combined_analysis.py** - Analyzes AI vs human agreement

**Files Added:**
- `AI_JUDGES_README.md` - Complete setup and usage guide
- `QUICKSTART_AI_JUDGES.md` - Quick 3-step guide
- Updated `requirements.txt` with API packages

---

### December 7, 2024: Experiment 02 Constraint Experiments
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
├── 01_bart_test.py                  # OLMo baseline
├── 02_constraint_experiments.py     # 4 variations runner
├── 03_ai_judges.py                  # AI judge evaluation ✨ NEW
├── 04_teen_review_generator.py      # Teen A/B comparisons ✨ NEW
└── 05_combined_analysis.py          # AI + human analysis ✨ NEW

results/
├── 01_bart_test_20251204_211238.json      # Baseline (1,060 tokens)
├── 02a_temp_0.5_20251207_090043.json      # Lower temp
├── 02b_temp_1.0_20251207_090153.json      # Higher temp
├── 02c_natural_constraint_20251207_090308.json  # Constraint
├── 02d_style_anchor_20251207_090355.json   # Style anchor ⭐
└── bart_test_review_template.csv          # Judge review template (legacy)

blog-drafts/ (gitignored)
├── 01-introducing-the-bart-test.md  # Post 1 (draft complete)
├── 02-finding-the-sweet-spot.md     # Post 2 (draft complete)
├── SERIES-OUTLINE.md                 # Full series plan
└── PRESENTATION-IDEAS.md             # Conference talk notes
```

---

## Current State

### What We Know (Dec 17, 2024)
- ✅ **Hybrid evaluation works** - AI + human judges agree on winners
- ✅ **"Trying too hard" is universal** - All OLMo outputs over-index on slang
- ✅ **Dated slang identified** - "no cap" and "vibe" feel old to teens
- ✅ **Emoji insight** - Core set is 😂😭🔥🥀, avoid uncommon ones
- ✅ **Blog posts drafted** - Parts 1-3 ready to publish

### Critical Open Question
**Does the prompt cause the problem or is it OLMo-specific?**

Need to test: Does baseline prompt make ALL models "try too hard" or just OLMo?

### Strategic Decision Made
**Committing to Option B: Benchmark (not prompt engineering)**
- Same prompt for all models
- Compare natural performance across models
- Build leaderboard showing who handles cultural fluency best
- See: `/Users/bartgottschalk/Projects/mosaic-mesh-strategic-planning/artifacts/02_active_workstreams/bart_test_strategic_plan.md`

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

### AI Judges Experiment (Part 4) - ✅ BUILT, READY TO TEST
1. ✅ **API client scripts** - Created `03_ai_judges.py`
2. ✅ **Judge prompt** - Same 1-10 rubric as humans
3. ⏳ **Run on Experiment 02** - Ready to execute (need API keys)
4. ⏳ **Teen A/B validation** - Scripts ready (`04_teen_review_generator.py`)
5. ⏳ **Analyze agreement** - Script ready (`05_combined_analysis.py`)
6. ⏳ **Write blog post #4** - "When AI Judges AI Slang"

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

# Install new dependencies (if needed)
pip install -r requirements.txt

# Set up API keys (add to ~/.bashrc or ~/.zshrc)
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
export GOOGLE_API_KEY="..."

# Run AI judges on Experiment 02 (NEW!)
python experiments/03_ai_judges.py

# Generate teen review sheets (NEW!)
python experiments/04_teen_review_generator.py

# Analyze AI + human agreement (NEW!)
python experiments/05_combined_analysis.py

# Run baseline test
python experiments/01_bart_test.py

# Run constraint experiments (all 4 variations)
python experiments/02_constraint_experiments.py
```

---

## Next Session: Critical Path

### Immediate Action (Required Before Locking Methodology)

**Experiment 03: Cross-Model Baseline Test**

**Goal**: Answer "Is it the prompt or the model?"

**Method**: Run EXACT baseline prompt on:
1. GPT-4o (OpenAI API)
2. Claude 3.5 Sonnet (Anthropic API)
3. Gemini Pro (Google API)

**Questions to Answer:**
- Do they also "try too hard" with slang?
- Do they also use dated terms ("no cap", "vibe")?
- Or do they naturally code-switch better than OLMo?

**Decision Point:**
- If all 3 struggle → Consider modifying prompt before locking
- If 1-2 handle it well → Lock baseline prompt as canonical

**Timeline**: ~2 hours to run, ~$15 in API costs

**After This**: We can confidently lock the methodology

---

### Short-Term Path (Next 2-3 Weeks)

**1. Lock Methodology**
- Create `METHODOLOGY.md` with canonical prompt, rubric, process
- Mark as immutable for fair cross-model comparison
- Document in blog post explaining the choice

**2. Publish Blog Series**
- Part 1: "Introducing the Bart Test"
- Part 2: "Finding the Sweet Spot" (updated with judge results)
- Part 3: "What the Teen Judges Said" (draft complete)
- Drive traffic to GitHub repo

**3. Test 3 More Models**
- With locked methodology
- Build initial 6-model leaderboard
- Publish individual model reviews

**4. Launch Static Site**
- bart-test.mosaicmeshai.com
- Simple landing page with methodology + leaderboard
- S3 + CloudFront hosting

---

### Key Files for Context

**Strategic Planning** (Private):
- `/Users/bartgottschalk/Projects/mosaic-mesh-strategic-planning/artifacts/02_active_workstreams/bart_test_strategic_plan.md`
- Complete business strategy, phased rollout, success metrics
- Read this FIRST in next session for full context

**Blog Drafts** (Private, gitignored):
- `blog-drafts/01-introducing-the-bart-test.md` - Part 1 (ready)
- `blog-drafts/02-finding-the-sweet-spot.md` - Part 2 (updated with results)
- `blog-drafts/03-what-the-teen-judges-said.md` - Part 3 (NEW, draft complete)

**Results** (Public repo):
- `results/human_reviews_20251217.md` - Teen feedback analysis
- `results/03_ai_judges_20251215_130645.json` - AI judge scores

**Documentation**:
- `AI_JUDGES_README.md` - Complete hybrid eval system guide
- `QUICKSTART_AI_JUDGES.md` - 3-step quick start

---

### Important Context from This Session

**Teen Reviewers:**
- J (Teen #1): Your daughter, gave "zoo not duck" metaphor
- R (Teen #2): Your daughter, technical context barrier
- N (Teen #3): Friend's kid (Jen's son), received $15 Starbucks gift card, approved for using feedback

**Key Insights Discovered:**
1. "Trying too hard" = universal problem across all OLMo outputs
2. Slang has a half-life - "no cap" and "vibe" already dated
3. Emoji currency - 😂😭🔥🥀 are current core set
4. Natural code-switching > slang density
5. Asterisks for actions feel artificial

**Strategic Decisions:**
1. ✅ Benchmark approach (not prompt engineering)
2. ✅ Hybrid evaluation (AI pre-screen + human validation)
3. ✅ Brand-building IP (not direct revenue)
4. ⏳ Canonical prompt decision (pending Experiment 03)

**Business Integration:**
- Part of Mosaic Mesh AI brand
- Supports courses, consulting, speaking
- See mosaicmeshai.com for full context
- StartUpWebApp fork for Phase 4 interactive platform

---

### Questions to Ask User When Resuming

1. **Ready to run Experiment 03?** (Test GPT/Claude/Gemini with baseline)
2. **Blog post timing?** Publish now or wait until methodology locked?
3. **Static site priority?** Build now or after testing 5-6 models?
4. **Teen recruiter expansion?** Keep current 3 or recruit more?

---

## Resources & Links

**Public:**
- **GitHub Repo**: https://github.com/bart-mosaicmeshai/bart-test
- **Business Site**: https://www.mosaicmeshai.com
- **About**: https://www.mosaicmeshai.com/about
- **Courses**: https://www.mosaicmeshai.com/ai-courses
- **Services**: https://www.mosaicmeshai.com/services

**Private:**
- **Strategic Plan**: `/Users/bartgottschalk/Projects/mosaic-mesh-strategic-planning/artifacts/02_active_workstreams/bart_test_strategic_plan.md`
- **Blog Drafts**: `blog-drafts/` (gitignored)

**Inspiration:**
- [Simon Willison's OLMo 3 post](https://simonwillison.net/2025/Nov/22/olmo-3/)

---

**Last Updated**: December 17, 2024
**Next Session Start**: Read strategic plan first, then ask about Experiment 03
