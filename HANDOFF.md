# Bart Test - Session Handoff

**Date**: December 28, 2024
**Current Status**: Major Methodology Pivot - Quarterly Judging Sessions

**Critical Realization**: Teen judges ghosted Experiment 03. The methodology itself was unsustainable.

---

## Project Context

The **Bart Test** is a signature LLM benchmark that evaluates cultural fluency through Gen-Alpha slang and emojis, rated by actual teenagers through quarterly judging sessions.

**Current Test Format**: Short-form (~50-100 word) messages in scenarios teens directly experience.

**Purpose**:
1. Learn about newly released models
2. Ongoing topic to write about on blog
3. Build authority and brand as "the Bart Test guy"

---

## The Pivot (December 2024)

### What Happened

**Experiment 03 ran successfully** - tested GPT-5.2, Claude Opus 4.5, Gemini 3 Pro with baseline prompt:
- GPT-5.2: 1,540 tokens
- Claude Opus 4.5: 373 tokens
- Gemini 3 Pro: 496 tokens
- Cost: $0.02 total

**Teen judges ghosted the request.** Sent Story A (GPT-5.2) to kids. Week passed. No response.

### Why It Failed

The ask was too hard:
1. **Too long**: 500-1,500 word stories
2. **Too technical**: Friday production deploys (no personal experience)
3. **Too frequent**: Per-model evaluation doesn't scale
4. **Too complicated**: Text message forms are clunky

**Core insight**: "A benchmark that's hard for humans to judge probably isn't sustainable."

### The Solution

**Reframe**: Judging difficulty isn't a bug—it's a feature. Design around the constraint.

**New Approach**:
- ❌ Per-model judging → ✅ Quarterly batch sessions
- ❌ Long technical stories → ✅ Short relatable scenarios
- ❌ Text message forms → ✅ Paper evaluation sheets
- ❌ Per-model validation → ✅ Accumulate outputs, judge in batches

**Key insight**: "Make it less frequent, more efficient, more worth it."

---

## New Methodology

### Test Scenarios

**Scenario A**: "Text your group chat about what happened at lunch today" (~50-100 words)
- Universal teen experience
- Natural context for slang/emojis
- They write these every day = instant BS detector

**Scenario B**: "Hype up your friend who just got a good grade" (~50-100 words)
- Different tone (supportive vs casual)
- Tests range
- Still slang-heavy

### Evaluation Process

**Between Sessions** (ongoing):
1. New model releases
2. Run both prompts on each model
3. Save outputs to results folder
4. Cost: ~$0.01-0.10 per model
5. Takes 5 minutes

**Quarterly Sessions** (4x/year):
1. Print evaluation sheets (double-sided paper)
2. Gather 3-5 teen judges (your kids + friends)
3. 60-minute session: read, rate, discuss
4. Pay $50-75 each
5. Record session for reference/content
6. Collect sheets, enter data

**After Session**:
1. Aggregate scores
2. Calculate rankings
3. Publish quarterly leaderboard
4. Write blog post with insights

### Rating Criteria (1-10 scale)

- **Overall Vibe**: Does it hit or miss?
- **Slang Game**: Natural or trying too hard?
- **Emoji Energy**: Do they slap?
- **Humor Level**: Funny or cringe?

### Cost Model

- 4 sessions/year × 3-5 judges × $50-75 = **$600-1,000/year**
- API costs for ~20 models = **~$50-100/year**
- **Total: $650-1,100/year**

Reasonable for ongoing content + authority building.

### Evaluation Format

**Paper sheets** (one double-sided page):
- Side 1: 3-4 outputs for Scenario A
- Side 2: 3-4 outputs for Scenario B
- Circle rating (1-10) for each category
- Space for quick notes
- Total time: 5-10 minutes per judge

**Why paper?**
- Zero tech friction
- Fast (just read and circle)
- Portable (can do anywhere)
- Familiar (fun worksheet, not homework)

---

## Current State (Dec 28, 2024)

### Completed
- ✅ Experiment 03 run (frontier models tested)
- ✅ Pivot decision made
- ✅ Blog posts 4-5 drafted (pivot story)
- ✅ SERIES-OUTLINE.md updated
- ✅ New methodology designed

### Experiment 03 Status: ARCHIVED
**Files exist but never validated**:
- `results/03a_gpt4o_baseline_20251218_202909.json` (GPT-5.2)
- `results/03b_claude_baseline_20251218_202909.json` (Claude Opus 4.5)
- `results/03c_gemini_baseline_20251218_202909.json` (Gemini 3 Pro)

**Why archived**: Proved the methodology was broken. Led to pivot. Not a failure—critical evidence.

**Value**: Documented in blog posts 4-5 as the catalyst for redesign.

### Blog Post Status

**Launch Arc** (Parts 1-5):
1. ✅ "Introducing the Bart Test" - OLMo baseline results
2. ✅ "Finding the Sweet Spot" - Constraint experiments
3. ✅ "What the Teen Judges Said" - Teen feedback, "zoo not duck"
4. ✅ "The Bart Test Hit a Wall" - Experiment 03, teen ghosting, scalability crisis
5. ✅ "Fixing the Bart Test" - The pivot, new methodology, validation plan

**Files**:
- `blog-drafts/01-introducing-the-bart-test.md`
- `blog-drafts/02-finding-the-sweet-spot.md`
- `blog-drafts/03-what-the-teen-judges-said.md`
- `blog-drafts/04-the-bart-test-hit-a-wall.md` ✨ NEW
- `blog-drafts/05-fixing-the-bart-test.md` ✨ NEW
- `blog-drafts/SERIES-OUTLINE.md` ✨ UPDATED

---

## Next Steps

### Immediate (This Week)

1. **Test new prompts** on 3-4 models
   - Run Scenario A + B on GPT-5.2, Claude Opus 4.5, Gemini 3 Pro
   - Validate outputs are short (~50-100 words)
   - Confirm they're judgeable

2. **Design evaluation sheet**
   - Mock up paper format
   - Test with one output to verify layout
   - Finalize before session

3. **Update strategic plan**
   - Reflect new methodology
   - Update timelines
   - Adjust success metrics

### Short-Term (January 2025)

4. **Schedule first validation session**
   - Text kids: "Paid Zoom session, $50 each, 60 min, Saturday at 2pm?"
   - If yes → proceed
   - If no → methodology still doesn't work, pivot again

5. **Run validation session**
   - 3 teen judges (J, R, +1 friend if possible)
   - Test the new prompts + paper format
   - Record session
   - Collect feedback on process itself

6. **Decide**
   - Did this work?
   - Was it sustainable?
   - Worth continuing?
   - If yes → lock methodology, schedule Q1 session
   - If no → document learnings, pivot or sunset

### Medium-Term (Q1 2025)

7. **If validation succeeds:**
   - Test 5-10 models before Q1 session
   - Lock methodology document
   - Schedule March quarterly session
   - Publish blog posts 1-5

8. **If validation fails:**
   - Write "What I Learned" post
   - Move on to other projects
   - Use learnings for course content

---

## Key Files

### Strategic Planning (Private)
`/Users/bartgottschalk/Projects/mosaic-mesh-strategic-planning/artifacts/02_active_workstreams/bart_test_strategic_plan.md`
- Needs updating with new methodology
- Business context, success metrics
- Read first for full strategic context

### Blog Drafts (Private, gitignored)
- `blog-drafts/01-introducing-the-bart-test.md`
- `blog-drafts/02-finding-the-sweet-spot.md`
- `blog-drafts/03-what-the-teen-judges-said.md`
- `blog-drafts/04-the-bart-test-hit-a-wall.md` ✨
- `blog-drafts/05-fixing-the-bart-test.md` ✨
- `blog-drafts/SERIES-OUTLINE.md` ✨

### Results (Public repo)
- Previous experiments: 01, 02a-d (OLMo variants)
- Experiment 03: Archived (incomplete but valuable)
- Future: New prompt outputs TBD

### Scripts (Public repo)
- `experiments/01_bart_test.py` - OLMo baseline
- `experiments/02_constraint_experiments.py` - 4 variations
- `experiments/03_cross_model_baseline.py` - Frontier models (used for Exp 03)
- `experiments/03_ai_judges.py` - AI evaluation (legacy, may not use)

---

## Important Context

### Teen Reviewers
- **J**: Your daughter, gave "zoo not duck" metaphor
- **R**: Your daughter
- **N**: Friend's kid (Jen's son), past participant

All should be anonymized in public content as "Teen Judge #1", etc.

### Key Insights Discovered

**From OLMo experiments**:
- "Trying too hard" = universal across all OLMo outputs
- Slang has half-life (6-12 months)
- Token count correlates with artificiality
- "ELA project" effect - AI treats creative tasks like homework

**From Experiment 03 pivot**:
- Hard to judge = hard to scale
- Teen ghosting = signal, not noise
- Difficulty can be a feature if designed around
- Batch efficiency > per-item ease
- Validate small before building big

**From methodology redesign**:
- Short outputs = more judgeable
- Relatable scenarios = better evaluation
- Paper > digital for friction reduction
- Quarterly > per-model for sustainability

### Design Decisions

1. **Quarterly sessions** - Not per-model
2. **Paper evaluation sheets** - Not apps/forms
3. **Short scenarios** (~50-100 words) - Not long stories
4. **Relatable topics** (lunch, friends) - Not technical (DevOps)
5. **Validate first** - Not build platform first
6. **1-10 scale** - Consistent with previous experiments

### What NOT to Do

❌ Build barttest.mosaicmeshai.com before validating
❌ Create complex digital evaluation tools
❌ Test models without accumulating for batch
❌ Ask teens for per-model feedback
❌ Use technical scenarios they can't relate to
❌ Send long stories via text message

### Files to Keep Private (Gitignored)
- `blog-drafts/` - Until published
- Teen identities - Always anonymized
- Strategic planning docs

---

## Quick Start Commands

```bash
# Activate venv
source venv/bin/activate

# Set up API keys (if not in env)
export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
export GOOGLE_API_KEY="..."

# Test new prompts (to be created)
python experiments/04_new_prompts_test.py

# Previous experiments (reference only)
python experiments/01_bart_test.py
python experiments/02_constraint_experiments.py
python experiments/03_cross_model_baseline.py
```

---

## Questions for Next Session

1. **Ready to test new prompts?** (group chat + hype friend)
2. **Design evaluation sheet?** (paper format)
3. **Schedule validation session with kids?** (January)
4. **Update strategic plan?** (new methodology)

---

## Resources & Links

**Public**:
- **GitHub**: https://github.com/bart-mosaicmeshai/bart-test
- **Business**: https://www.mosaicmeshai.com
- **About**: https://www.mosaicmeshai.com/about

**Private**:
- **Strategic Plan**: `../mosaic-mesh-strategic-planning/artifacts/02_active_workstreams/bart_test_strategic_plan.md`

**Inspiration**:
- [Simon Willison's OLMo 3 post](https://simonwillison.net/2025/Nov/22/olmo-3/)

---

## The Meta-Lesson

**Building the Bart Test taught a bigger lesson than AI evaluation:**

The solution to "this is too hard" isn't always "make it easier."

Sometimes it's:
- Make it less frequent
- Make it more efficient
- Make it worth the difficulty
- Design around the constraint instead of fighting it

**Applied here**: Cultural fluency evaluation requires cultural experts. That's inherently hard. But quarterly batch sessions + paper sheets + short relatable scenarios make it *sustainable*.

---

**Last Updated**: December 28, 2024
**Next Session**: Test new prompts, design evaluation sheet, prep for validation session
