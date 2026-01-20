# Experiment 05 Key Findings - For Blog Post Part 9

**Date:** December 30, 2024
**For:** Blog post "Part 9: When the Test Gets Too Easy"

---

## The Quick Answer

**Did the test get too easy?** It depends on whose perspective you take.

- **Judge #1's view:** Yes (scores clustered 8-10, lots of praise)
- **Judge #2's view:** No (no scores above 8, maintained critical stance)
- **Overall benchmark:** No (differentiation nearly doubled)

---

## Model Rankings - Experiment 05

**2-Judge Average (4 categories):**

1. **Claude Opus 4.5: 7.69** ⭐ (+1.94 vs Exp 04, +33.7%)
2. **GPT-5.2: 7.06** (+1.18 vs Exp 04, +20.1%)
3. **OLMo 3 32B Think: 6.19** (-0.06 vs Exp 04, -1%)
4. **Llama 3.1 8B: 5.75** (+0.50 vs Exp 04, +9.5%)
5. **Qwen3 14B: 4.94** ❌ (-1.69 vs Exp 04, -25.5%)

**Spread: 2.75 points** (vs Exp 04: 1.38 points) - **Differentiation nearly DOUBLED**

---

## Judge #1's Top Scores (The "8-10 Clustering")

**Outputs scoring 8+ on Overall Vibe:**
- Claude Scenario A: 9/8/7/9 - "This one paints a really good picture :)"
- Claude Scenario B: 8/10/8/10 - "This sounds like something I'd write with, like excessive slang as a joke" + smiley
- OLMo Scenario B: 9/10/9/9 - "omg, so close to perfect, I'd just take out this one sentence"
- GPT Scenario A: 8/7/8/10 - "That's a really cool story :)"
- Llama Scenario A: 7/9/7/10 - "really, I want to see this" (humor)

**This IS the experience described in Part 9's opening: "8s, 9s, and 10s across the board"**

---

## Judge #2's Scores (The Conservative Counterbalance)

**Highest scores:** All ≤8
- No 9s or 10s on any output
- Maintained critical stance
- Complained throughout evaluation
- Unwilling to continue

**This prevented overall score inflation and maintained benchmark difficulty**

---

## What Actually Happened (The Nuanced Story)

### Winners (Constraints Helped)

**Claude Opus 4.5:** +1.94 points (+33.7%)
- Fixed: Eliminated markdown formatting (# headers, paragraph breaks)
- Fixed: Tighter word count improved coherence
- Result: Highest-rated model overall

**GPT-5.2:** +1.18 points (+20.1%)
- Fixed: Eliminated asterisks
- Fixed: Scenario A dramatically improved (+3.0 points)
- Problem: Scenario B declined (-0.62) due to "him/her/them" overcorrection

### Losers (Constraints Hurt)

**Qwen3 14B:** -1.69 points (-25.5%)
- **Catastrophic coherence collapse in Scenario A**
- Judge #1: "Um wait, I literally have no idea how any of the consecutive peices flow."
- Couldn't score humor: "literally didn't know what happened, so idk"
- Hypothesis: Prescriptive "make it clear" instruction confused the thinking model

**OLMo 3 32B:** Scenario B regressed
- Exp 04 (26 words): 7.9 avg - "this would be something my friends would write"
- Exp 05 (59 words): 6.38 avg - Lost the authenticity win
- Shows: Brevity = authenticity, but we chose depth over authenticity

---

## Key Insights

### 1. The American Ninja Warrior Hypothesis Result

**Hypothesis:** Would tighter constraints improve differentiation or make the test too easy?

**Answer:** BOTH happened, depending on the model.

- Differentiation INCREASED overall (2.75 vs 1.38 point spread)
- Some models got better (Claude, GPT)
- Some models got worse (Qwen catastrophically, OLMo on one scenario)
- **This is GOOD benchmark behavior** - reveals model-specific responses to constraints

### 2. Explicit Goals Work (For Most Models)

**Humor scores with explicit "make it funny" instruction:**
- Claude: +55% (5.0 → 7.75)
- Llama: +64% (3.5 → 5.75)
- GPT: +12% (6.5 → 7.25)

**Lesson:** LLMs respond to explicit instructions, even for creative/subjective tasks

### 3. But Prescriptive Constraints Can Backfire

**Qwen3's coherence collapse shows:**
- Some models (especially thinking models) may be confused by too much guidance
- "Make it clear and make sense" → complete incoherence for Qwen
- One-size-fits-all prompts don't work across all architectures

### 4. The Authenticity Paradox Persists

**The only authentic output remains:**
- Exp 04 OLMo Scenario B (26 words)
- Judge #2: "this would be something my friends would write, just without the 'AF'"

**All 50-60 word outputs in Exp 05:**
- More testable (enough content to evaluate)
- Less authentic (length signals AI generation)
- This tradeoff is fundamental

---

## Judge Burnout (Critical Operational Finding)

**Judge #2:** Completed evaluation but complained throughout, unwilling to continue

**Context:**
- Experiment 04: Dec 28, 2024
- Experiment 05: Dec 30, 2024
- **2 sessions in 3 days = burnout**

**Lesson:** Quarterly cadence isn't optional, it's survival

---

## How to Use This Data in Part 9

### Option 1: Lead with Judge #1's Experience, Then Reveal Nuance

> "I glanced at the scores from Judge #1: 8s, 9s, and 10s across the board. My first reaction wasn't excitement. It was concern.
>
> Had I made the test too easy?
>
> But when I looked at the full data, I found something more interesting. Judge #2's scores told a different story—no scores above 8, critical feedback, maintained skepticism. And the overall spread between models had nearly doubled from Experiment 04.
>
> The test didn't get uniformly easier. Some models thrived with the tighter constraints (Claude +34%, GPT +20%). Others collapsed entirely (Qwen -26%, with complete coherence failure). Differentiation increased, not decreased.
>
> This was actually what a good benchmark should do: reveal how different models respond to the same challenge."

### Option 2: Focus on Individual Judge Perspectives as the Story

> "Two judges, same outputs, completely different experiences.
>
> Judge #1 saw improvement everywhere—8s, 9s, 10s, praise for 'cool stories' and 'so close to perfect' outputs. From their perspective, the refined prompts had worked. The outputs were better.
>
> Judge #2 saw something else. Conservative scores, no 9s or 10s, and consistent criticism. From their perspective, nothing had fundamentally changed. The AI was still trying too hard.
>
> Both were right. The question is: which perspective reveals more about the benchmark's value?"

### Option 3: Keep It Simple (Sacrifice Nuance for Narrative Clarity)

> "Judge #1's scores clustered in the 8-10 range. Much higher than Experiment 04. Fewer critical comments. More praise.
>
> I'd refined the prompts to reduce noise and improve differentiation. Instead, I'd made the course easier. More models were succeeding—which sounds good until you realize it means the test is revealing less about their actual capabilities.
>
> The American Ninja Warrior problem had materialized."

---

## Supporting Data Points for Part 9

**Word count tightened:**
- Exp 04: 26-68 words (wide variance, models struggled differently)
- Exp 05: 44-66 words (narrower range, closer to target 50-60)

**Formatting issues reduced:**
- No more Claude paragraph breaks
- No more GPT asterisks
- No more Llama "in the comments below"
- Constraints eliminated model quirks

**But one catastrophic failure:**
- Qwen3 Scenario A: Complete incoherence
- Shows the test can still break models badly
- This IS valuable differentiation

---

## The Strategic Question Part 9 Should Pose

> "Should I:
> - Lock in Experiment 04's prompt as the baseline? (harder, more differentiation through struggle)
> - Lock in Experiment 05's prompt as the baseline? (some models improved, but overall differentiation actually increased)
> - Keep iterating to find the sweet spot?
>
> I don't have the answer yet. But at least now I know the question."

**Actual answer (that we know now but Part 9 doesn't reveal):**
Neither. The project paused due to judge burnout and unclear value proposition. But that's the story for Parts 7-8, not Part 9.

---

## Files Reference

- **Full ratings data:** `evaluation_sheets/20251230/experiment_05_ratings_20251230.json`
- **Detailed comparison:** `evaluation_sheets/20251230/experiment_04_vs_05_comparison.md`
- **This summary:** `evaluation_sheets/20251230/part_9_key_findings.md`

---

**Created:** December 30, 2024
**Status:** Ready for blog post integration
