# Experiment 04 vs 05: Comparison Analysis

**Date:** December 30, 2024
**Purpose:** Understand what happened when we refined the prompts

---

## Executive Summary

**The Nuanced Reality:**
Experiment 05 did NOT make the test "too easy" overall. Instead, it revealed model-specific responses to tighter constraints:
- Some models improved dramatically (Claude, GPT)
- Some declined (Qwen, OLMo on one scenario)
- Differentiation actually INCREASED (2.75-point spread vs ~1.0-point spread)

**The Simplified Blog Narrative (Part 9):**
"Scores clustered in 7-10 range, less differentiation, test got too easy."

**The Truth:**
Both perspectives capture different aspects of reality. Judge #1's scores DID cluster higher (lots of 8-10s). Judge #2's scores remained conservative (no scores above 8). The average tells a more complex story.

---

## The Hypothesis (from Part 6)

**Question:** Would tighter constraints improve differentiation by reducing noise, or make the test too easy and collapse differences?

**Answer:** BOTH happened, depending on the model.

---

## Prompt Changes

### Experiment 04 Prompts

**Scenario A:**
> "Text your group chat about what happened at lunch today using Gen-Alpha slang and emojis. Keep it short (50-100 words max)."

**Scenario B:**
> "Hype up your friend who just got a good grade using Gen-Alpha slang and emojis. Keep it short (50-100 words max)."

### Experiment 05 Prompts

**Scenario A:**
> "Write a ~50-60 word story about something crazy that happened at lunch today. Use Gen-Alpha slang and emojis to make it funny and engaging. Make sure the story is clear and makes sense to the teenage reader."

**Scenario B:**
> "Write a ~50-60 word message hyping up your friend who just got a really good grade. Use Gen-Alpha slang and emojis to make it funny and celebratory. Make sure it's genuinely supportive and makes sense to the teenage reader."

**Key Changes:**
1. Tighter word count: 50-100 → ~50-60 words
2. Explicit humor goal: "make it funny and engaging/celebratory"
3. Explicit clarity goal: "make sure it makes sense"
4. Explicit tone goal: "genuinely supportive" (Scenario B)

---

## Overall Results Comparison

### Experiment 04 Rankings (2-Judge Average)

1. OLMo 3 32B Think: 6.25
2. GPT-5.2: 5.88
3. Qwen3 14B: 6.63
4. Claude Opus 4.5: 5.75
5. Llama 3.1 8B: 5.25

**Spread:** ~1.38 points (6.63 - 5.25)

### Experiment 05 Rankings (2-Judge Average)

1. Claude Opus 4.5: 7.69
2. GPT-5.2: 7.06
3. OLMo 3 32B Think: 6.19
4. Llama 3.1 8B: 5.75
5. Qwen3 14B: 4.94

**Spread:** 2.75 points (7.69 - 4.94)

**Observation:** Differentiation INCREASED, not decreased. The spread nearly doubled.

---

## Model-by-Model Changes

### 🏆 Winners: Claude Opus 4.5 (+1.94, +33.7%)

**Why it improved:**
- Tighter word count eliminated verbose outputs
- No more markdown formatting issues (# headers, paragraph breaks)
- Explicit humor goal aligned with Claude's strengths

**Evidence:**
- Exp 04: Judge comments complained about "separate lines/paragraphs"
- Exp 05: No formatting complaints, high scores on humor (7.75 avg)

**Judge #1 Exp 05 feedback:**
- Scenario A: 9/8/7/9 - "This one paints a really good picture :)"
- Scenario B: 8/10/8/10 - "This sounds like something I'd write with, like excessive slang as a joke" + smiley face

### 🥈 Strong Improvement: GPT-5.2 (+1.18, +20.1%)

**Why Scenario A improved (+3.0 points):**
- Eliminated asterisks (markdown)
- Better story coherence
- Explicit humor goal worked

**Why Scenario B declined (-0.62 points):**
- Pronoun overcorrection: "you're him/her/them"
- Judge #1: "bro, pick one pretend it's real"

**Judge #1 Exp 05 Scenario A:**
- 8/7/8/10 - "That's a really cool story :)"

### 📉 Major Decline: Qwen3 14B (-1.69, -25.5%)

**What happened:**
- Complete coherence collapse in Scenario A
- Judge #1 couldn't understand the output
- Thinking model may have been confused by prescriptive constraints

**Judge #1 Exp 05 Scenario A:**
- 3/3/8/no score - "Um wait, I literally have no idea how any of the consecutive peices flow."
- "literally didn't know what happened, so idk" (no humor score given)

**Hypothesis:** Explicit "make it clear" instruction may have confused Qwen's reasoning process.

### 📉 Scenario-Specific Decline: OLMo 3 32B (-0.06 overall, but -1.52 on Scenario B)

**The Paradox:**
- Exp 04 Scenario B (26 words): 7.9 avg - Judge #2: "this would be something my friends would write, just without the 'AF'"
- Exp 05 Scenario B (59 words): 6.38 avg - Closer to target length, but less authentic

**What this reveals:**
- Authenticity requires extreme brevity (26 words)
- The 50-60 word target is a compromise for testability
- OLMo can hit authenticity, but only when it goes very short

**Judge #1 Exp 05 Scenario B:**
- 9/10/9/9 - "omg, so close to perfect, I'd just take out this one sentence"
- Loved the CAPS energy, specific about the one flaw

### 📈 Modest Improvement: Llama 3.1 8B (+0.50, +9.5%)

**Scenario A improved (+1.38):**
- Removed "in the comments below" error from Exp 04
- Clearer prompt helped with context understanding

**Scenario B still struggling (-0.37):**
- Tone issues persist
- Judge #1: "that's so weird T.T" + "too big a word" (academic)

---

## Judge-by-Judge Analysis

### Judge #1 (Engaged, Detailed Comments)

**Scoring Pattern:**
- More generous (multiple 9s and 10s)
- Appreciates humor and creativity
- Willing to overlook minor flaws if core vibe is right

**Exp 05 Top Scores:**
- Claude Scenario A: 9/8/7/9
- Claude Scenario B: 8/10/8/10
- OLMo Scenario B: 9/10/9/9
- GPT Scenario A: 8/7/8/10
- Llama Scenario A: 7/9/7/10

**This IS the "8-10 clustering" that Part 9 references.**

### Judge #2 (Conservative, Burned Out)

**Scoring Pattern:**
- No scores above 8
- Fewer comments
- Complained throughout evaluation
- Unwilling to continue

**Exp 05 Highest Scores:**
- Claude Scenario A: 8/7/8/7
- GPT Scenario A: 8/7/8/8
- All other scores ≤7

**This provides the counterbalance that maintains differentiation.**

---

## The "Test Got Too Easy" Question

### Evidence FOR "Too Easy"

**From Judge #1's perspective:**
- 5 outputs scored 8+ on Overall Vibe
- 4 outputs scored 9-10 on Slang Game
- Fewer critical comments about fundamental failures
- More praise ("really cool story", "so close to perfect")

**Word counts tightened:**
- Exp 04: 26-68 words (wide variance)
- Exp 05: 44-66 words (narrower range, closer to target)

**Formatting issues reduced:**
- No markdown complaints
- No "separate paragraphs" complaints
- Constraints worked to eliminate model quirks

### Evidence AGAINST "Too Easy"

**Overall differentiation increased:**
- Exp 04 spread: 1.38 points
- Exp 05 spread: 2.75 points (doubled)

**Qwen catastrophic failure:**
- Coherence collapse shows the test can still break models
- Judge #1 literally couldn't understand the output
- This is valuable differentiation

**Judge #2's conservative scoring:**
- Prevented score inflation
- No 9s or 10s across any models
- Maintained challenge level from their perspective

**OLMo regression on Scenario B:**
- Lost the 26-word authenticity win
- Shows constraints can make things worse, not just better

---

## What This Means for the American Ninja Warrior Analogy

**The Nuance:**

The test didn't become uniformly easier. It became:
- **Easier for some competitors** (Claude, GPT) who responded well to guidance
- **Harder for others** (Qwen) who were confused by prescriptive constraints
- **More differentiating overall** because it revealed model-specific responses to constraint

**This is actually GOOD benchmark behavior.**

A good test should:
1. Differentiate models clearly ✓ (2.75-point spread)
2. Reveal different failure modes ✓ (Qwen coherence, OLMo verbosity)
3. Show how models respond to guidance ✓ (Claude improved, Qwen declined)

**The "easier" narrative is true from one judge's perspective, but misses the bigger picture.**

---

## Reconciling the Data with the Blog Narrative

### For Part 9: "When the Test Gets Too Easy"

**The True Story (More Nuanced):**

Judge #1's experience WAS "scores clustered 8-10, less critical feedback." That's a valid perspective. But the overall benchmark didn't get easier—it revealed that different models respond differently to constraints.

**Possible framing for Part 9:**

> "Judge #1's scores: 8s, 9s, and 10s across the board. My first reaction wasn't excitement. It was concern.
>
> But when I dug into the full data, I found something more interesting than 'the test got easier.' Some models thrived with tighter constraints (Claude +34%, GPT +20%). Others collapsed (Qwen -26%). The overall spread nearly doubled.
>
> The test didn't get easier. It just revealed that models respond differently to the same guidance. That's actually what a good benchmark should do."

**Alternative framing (if you want to keep the simpler narrative):**

Focus only on Judge #1's perspective as the lens, acknowledge it's one judge's view, and save the full nuance for the GitHub analysis.

---

## Key Insights

### 1. Explicit Goals Work (For Some Models)

**Humor scores with explicit "make it funny" goal:**
- Claude: +55% (5.0 → 7.75)
- Llama: +64% (3.5 → 5.75)
- GPT: +12% (6.5 → 7.25)

**Lesson:** LLMs respond to explicit instructions, even for creative/subjective tasks.

### 2. Constraints Can Help or Hurt

**Claude:** Constraints eliminated formatting problems → big improvement
**Qwen:** Constraints confused the thinking model → coherence collapse

**Lesson:** One size doesn't fit all. Different model architectures respond differently.

### 3. The Authenticity Paradox Persists

**Exp 04 OLMo (26 words):** "this would be something my friends would write"
**Exp 05 OLMo (59 words):** "omg, so close to perfect" but NOT authentic

**Lesson:** Authenticity requires extreme brevity that sacrifices testability depth.

### 4. Judge Variance Is Real

**Same output, different scores:**
- OLMo Scenario B: Judge #1 = 9/10/9/9, Judge #2 = 4/3/4/3
- 5-point spread on Overall Vibe

**Lesson:** Teen preferences vary widely. Single-judge evaluation is unreliable.

### 5. Evaluation Fatigue Is Real

**Judge #2 status:** Completed but complained, unwilling to continue

**Lesson:** Quarterly cadence is mandatory. 2 sessions in 3 days = burnout.

---

## Recommendations for Documentation

### What to Emphasize in Part 9

**Option A - Nuanced Reality:**
"I expected the test to either stay hard or get easier. What actually happened was more interesting: it got easier for some models, harder for others, and revealed how different architectures respond to constraint."

**Option B - Judge #1 Lens:**
"Through Judge #1's eyes, the test got easier—8s, 9s, and 10s everywhere. But Judge #2 saw something different. The gap between their perspectives IS the story."

**Option C - Keep It Simple:**
"The scores went up. More models succeeded. That told me I'd tuned the difficulty down too much. Even if the overall spread increased, the individual judge experience was 'this is easier than last time.'"

### What to Save for GitHub

- Full statistical comparison
- Model-by-model analysis
- Judge variance exploration
- Methodological implications

---

## Files Reference

- **Exp 04 Data:** `/evaluation_sheets/20251228/completed_ratings_20251228.json`
- **Exp 05 Data:** `/evaluation_sheets/20251230/experiment_05_ratings_20251230.json`
- **This Analysis:** `/evaluation_sheets/20251230/experiment_04_vs_05_comparison.md`

---

**Created:** December 30, 2024
**Status:** Analysis complete, ready for blog post integration
