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
- Side 1: 5 outputs for Scenario A
- Side 2: 5 outputs for Scenario B
- Mark rating (1-10) for each category (circle, X, fill-in - any method)
- Instructions include full prompt text for context
- "Feel free to write comments anywhere on the page"
- Total time: 5-10 minutes per judge

**HTML Generation** (automated by Claude agent):
- Agent reads mapping file + JSON outputs
- Generates HTML with all outputs, tracking codes, ratings
- Manually adjusts CSS spacing to fit exactly 2 pages
- Print directly or save as PDF

**Why paper?**
- Zero tech friction
- Fast (just read and mark)
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
- ✅ **Experiment 04 complete** - New prompts tested on 5 models (GPT-5.2, Claude, Llama, Qwen, OLMo)
- ✅ **Evaluation sheet generated** - HTML format, 2 pages, ready to print
- ✅ **PROCESS.md created** - Complete repeatable workflow documentation
- ✅ **Validation ready** - 2 printed sheets handed to kids for validation session

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

### Immediate (NOW - Dec 28, 2024)

1. **✅ VALIDATION SESSION COMPLETED** (Dec 28, 2024 evening)
   - Both kids completed evaluation sheets
   - Got ratings + written feedback
   - Process worked mechanically (paper format, completion)
   - **Judge J feedback:** "This sheet was much easier to do than the previous versions we tried"

2. **⚠️ CRITICAL META FEEDBACK (Pre-Data Entry)**

**From Teen Judge (before entering ratings):**

   a. **Length is fundamentally broken**: "No human Gen Alpha person writes such long posts" - The 50-100 word target is still too long. Length alone signals inauthenticity regardless of content quality.

   b. **Emoji density problem**: "No human uses so many emojis" - All AI outputs over-indexed on emoji usage even in short form.

   c. **Humor rubric confusion**: "What is the point of Humor Level? Is this supposed to be funny?" - Rubric category may not match scenario intent or teen expectations.

   d. **Compensation insight**: Friends would fill these out for "$5 cash" (not $50-75 gift cards) - Much lower barrier than planned.

**Implication:** Even before analyzing numeric ratings, fundamental methodology questions remain about output length, emoji density, and rubric design.

3. **IN PROGRESS: Data entry**
   - Enter 4 ratings per tracking code from both judges
   - Capture written comments from sheets
   - Analyze if ratings differentiate models despite meta concerns

4. **VALIDATION RESULTS:**
   - ✅ **Process mechanics: SUCCESS** - Paper format worked well, reasonable completion time, Judge J said "much easier than previous versions"
   - ⚠️ **Ratings differentiation: YES but complex** - Scores ranged 2-10, models differentiated, BUT huge inter-judge variance (6-point spreads on same outputs)
   - ⚠️ **Authenticity test: MOSTLY FAILED, one exception** - Meta feedback: all outputs too long, too many emojis. HOWEVER: Judge R gave OLMo Scenario B (26 words) a 10/9/10/7 - "this would be something my friends would write, just without the 'AF'"
   - ✅ **Judge willingness: YES** - Both completed, willing to continue, especially at $5 cash compensation

### Key Research Questions Emerging from Validation

**Question 1: Do ratings meaningfully differentiate models?**
- Status: INCONCLUSIVE - insufficient data
- Finding: Model averages cluster in 5.0-6.5 range (1.5-point spread)
- Finding: Variance WITHIN models (2-10 for OLMo) exceeds variance BETWEEN models
- To resolve: Would need more judges/sessions → costs time and money
- Decision: Can't conclude from 2 judges whether ratings provide meaningful signal

**Question 2: Is length THE critical variable for authenticity?**
- Status: KEY RESEARCH QUESTION - needs dedicated experiment
- Evidence: OLMo Scenario B (26 words) = only output to pass authenticity (10/9/10/7 from Judge R)
- Evidence: Both judges repeatedly commented "short is good"
- Evidence: All other outputs 35-85 words, all criticized as too long
- **Hypothesis to test: "If you constrained prompts to 15-30 words (instead of 50-100), would that fix the authenticity problem?"**
- Next experiment: Test same 5 models with 15-30 word constraint, run through same evaluation

**Question 3: Is inter-judge variance a feature or a bug?**
- Status: REFRAMED - doesn't matter for project goals
- 6-point spreads on same outputs (OLMo Scenario A: J=2, R=8)
- Could be: age differences, preferences, social circles, anything
- Would require sophisticated experimentation to isolate (not worth time/money)
- **KEY REFRAME: This is exploratory research for content, not scientific benchmark**
- Goal: Explore current LLM capabilities and write about what emerges
- Judge disagreement IS interesting content ("even teens disagree on authenticity")
- Qualitative insights more valuable than numeric precision
- Scores are "illustrative" not "definitive"

### Validation Decision: PARTIAL SUCCESS - Iterate on Prompts

**What worked:**
- ✅ Paper evaluation process (sustainable, low-friction, generates rich feedback)
- ✅ Judge engagement (willing to continue, especially at $5 cash)
- ✅ Qualitative insights valuable for content (regardless of numeric precision)

**What needs fixing:**
- ❌ Outputs too long/too many emojis (but ONE success case: OLMo 26 words)
- ❌ Prompt-rubric mismatch ("Humor Level" but prompt doesn't say "be funny")
- ❌ Unclear task definition for LLMs and judges

**Critical Strategic Pivot:**

**The Length/Depth Tradeoff:**
- Shorter messages = more authentic BUT too simple to test cultural fluency meaningfully
- Example: Real teen group chats are "short simple things that don't have enough depth"
- 13yo daughter's favorite cultural content: Long-form sketch (https://www.youtube.com/watch?v=Zf_125ApDvw) delivered by non-Gen-Alpha person
- **Decision: Optimize for "Can AI demonstrate cultural fluency in a meaningful way?" NOT "Can AI mimic authentic teen texting?"**

**Validation Target Shift:**
- OLD: "My friends would write that" (requires brevity that lacks depth)
- NEW: "Yeah, that was good use of slang and emojis. It wasn't cringy or try-too-hard."

**Humor as Core Element:**
- Humor is engaging for judges (makes evaluation fun)
- Humor is culturally subtle (good test of fluency)
- Decision: Make humor EXPLICIT in prompts (not emergent)
- Keep "Humor Level" in rubric, but align with prompt

### Next Steps: Experiment 05B - Reframe Scenarios with Clear Intent

**Approach:**
- Rewrite prompts to be explicit about goals (story, humor, cultural fluency, clarity)
- Keep 50-100 word range (complexity needed for meaningful test)
- Keep current 4-category rubric (aligned with new prompts)
- Make expectations clear to BOTH LLMs and judges

**Experiment 05B: Final Prompts**

**Design Principles:**
- ONE prompt shown to both LLM and judge (transparency, AI literacy education)
- Plain language teens understand
- Specific goals (funny, clear, supportive) without over-prescribing execution
- ~50-60 words (balance: enough depth to test fluency, short enough to avoid eye-rolls)

**Scenario A: Lunch Story**
```
Write a ~50-60 word story about something crazy that happened at
lunch today. Use Gen-Alpha slang and emojis to make it funny and engaging.
Make sure the story is clear and makes sense to the teenage reader.
```

**Scenario B: Hype Up Your Friend**
```
Write a ~50-60 word message hyping up your friend who just got a really
good grade. Use Gen-Alpha slang and emojis to make it funny and
celebratory. Make sure it's genuinely supportive and makes sense
to the teenage reader.
```

**Changes from Experiment 04:**
- Length: ~50-60 words (down from 50-100) - judges said "short is good"
- Explicit: "funny and engaging/celebratory" (aligns with Humor Level rubric)
- Explicit: "clear and makes sense to teenage reader" (addresses coherence issues)
- Explicit: "genuinely supportive" (addresses "kinda mean" feedback)
- Removed: Over-prescriptive language (not prompt engineering exercise)

**Keep Same:**
- 4-category rubric (Overall Vibe, Slang Game, Emoji Energy, Humor Level)
- Paper evaluation sheet format
- Same 5 models (GPT-5.2, Claude Opus 4.5, Llama 3.1 8B, Qwen3 14B, OLMo 3 32B)
- Same judges (J and R)

**Experiment 05 Status: COMPLETE - Awaiting Validation**

1. ✅ **Experiment 05 Outputs Generated** (Dec 30, 2024)

   **Scripts created:**
   - `experiments/05_new_prompts_test_frontier.py` (GPT-5.2, Claude Opus 4.5, Gemini 3 Pro)
   - `experiments/05_new_prompts_test_llama.py` (Llama 3.1 8B - requires LM Studio)
   - `experiments/05_new_prompts_test_qwen.py` (Qwen3 14B - requires LM Studio, thinking model)
   - `experiments/05_new_prompts_test_olmo.py` (OLMo 3 32B - requires LM Studio, reasoning model)

   **Run commands:**
   ```bash
   # Frontier models (API keys required)
   python experiments/05_new_prompts_test_frontier.py

   # Local models (load ONE at a time in LM Studio first)
   python experiments/05_new_prompts_test_llama.py
   python experiments/05_new_prompts_test_qwen.py    # Thinking model, ~8 seconds
   python experiments/05_new_prompts_test_olmo.py    # Reasoning model, ~30-60 seconds
   ```

   **All outputs generated successfully:**
   - 10 outputs total: 5 models × 2 scenarios
   - Files organized in `results/05_final_outputs/`
   - Qwen3 14B required increased max_tokens (1200) due to extensive thinking traces
   - Gemini 3 Pro blocked by recitation filter (same as Experiment 04)

   **Evaluation sheet created:**
   - Location: `evaluation_sheets/20251230/evaluation_sheet_20251230.html`
   - Mapping file: `evaluation_sheets/20251230/evaluation_sheet_mapping_20251230.json`
   - Format: Compact 2-page sheet (exactly 2 pages when printed)
   - Tracking codes: Randomized 6-character codes for blinding
   - Printed and ready for judges

2. ⏳ **Validation Session In Progress** (Dec 30, 2024 afternoon)
   - Judges: J and R (possibly J's friend as 3rd judge)
   - Compensation: $5 cash each
   - Status: Sheets printed, waiting for completion

3. **NEXT: Data Entry & Analysis**
   - Do shorter outputs score higher on authenticity?
   - Does explicit humor goal improve Humor Level ratings?
   - Do clearer prompts reduce coherence issues?
   - Do judges feel the outputs are "not cringy"?

3. ⏳ **Decide: Lock Methodology or Iterate Again**
   - If outputs meet validation target ("good use of slang/emojis, not cringy"): LOCK IT
   - If still issues: Diagnose and decide whether to iterate or pivot
   - Document learnings either way

### Medium-Term (Q1 2025)

**If Experiment 05B succeeds:**
4. Lock methodology in PROCESS.md (mark scenarios/prompts as final)
5. Test 5-10 additional models before Q1 session
6. Schedule March quarterly session
7. Publish blog posts 1-5 (including pivot story from Exp 04)

**If Experiment 05B reveals more issues:**
4. Decide: Another iteration or accept partial validation?
5. Write "What I Learned" series
6. Use learnings for course content (methodology iteration as teaching material)

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
- `experiments/04_new_prompts_test_frontier.py` - GPT, Claude, Gemini (new scenarios)
- `experiments/04_new_prompts_test_llama.py` - Llama 3.1 8B
- `experiments/04_new_prompts_test_qwen.py` - Qwen3 14B (thinking model)
- `experiments/04_new_prompts_test_olmo.py` - OLMo 3 32B Think

### Process Documentation
- `PROCESS.md` - Complete repeatable workflow for running the Bart Test
- `HANDOFF.md` - This file (session-to-session continuity)

### Evaluation Materials
- `evaluation_sheets/20251228/evaluation_sheet_20251228.html` - Current validation sheet
- `evaluation_sheets/20251228/evaluation_sheet_mapping_20251228.json` - Tracking codes to models

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

1. **Did the validation session work?** (waiting for kids to complete sheets)
2. **Do the ratings differentiate models?** (will know after data entry)
3. **Are these scenarios permanent or pivot again?** (depends on validation results)
4. **Update strategic plan?** (once methodology is locked)

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

**Last Updated**: December 30, 2024 (Afternoon - Experiment 05 Complete, Validation In Progress)
**Status**: Experiment 05 outputs generated, evaluation sheet printed, awaiting judge completion
**Next Session**: Data entry from Experiment 05 completed sheets, analyze if refined prompts worked
