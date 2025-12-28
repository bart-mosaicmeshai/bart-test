# The Bart Test

> **Note (January 2025):** The Bart Test methodology is being redesigned based on learnings from initial experiments. This document describes the original approach used in Experiments 01-02. See the [blog series](https://www.mosaicmeshai.com/blog) (launching Jan 7, 2025) for the full story of the pivot and new validation approach.

## Overview
A signature test for evaluating LLM reasoning, creativity, and cultural understanding through a blend of technical storytelling, Gen-Alpha slang, and emoji narrative.

## The Prompt

```
Tell the story of a developer deploying code to production on a Friday afternoon (and something goes wrong) using Gen-Alpha slang and emojis. Make it realistic and funny.
```

## Why This Test?

1. **Multi-dimensional evaluation**
   - Technical understanding (deployment, DevOps, production issues)
   - Cultural awareness (Gen-Alpha slang usage and accuracy)
   - Creative expression (emoji storytelling)
   - Narrative structure (beginning, middle, end)
   - Humor (relatable developer experience)

2. **Reasoning complexity**
   - Must understand developer workflows
   - Must know current slang and use it appropriately
   - Must map abstract concepts to visual emojis
   - Must balance technical accuracy with comedic timing

3. **Human judgment factors**
   - Visual appeal (emoji usage)
   - Slang authenticity (does it sound natural or forced?)
   - Technical credibility (would a developer find this realistic?)
   - Humor (does it land?)

## Scoring Rubric

### Human Judges (Primary - Ground Truth)

Teen judges rate on a 1-10 scale for each category:

**Overall Vibe (1-10)**
- Does it hit or completely miss?
- 1 = Completely cooked (cringe, trying way too hard)
- 10 = Actually bussin' (sounds natural, would pass as human)

**Slang Game (1-10)**
- Natural or trying too hard?
- 1 = Forced, incorrect, or very dated
- 10 = Uses terms correctly and naturally

**Emoji Energy (1-10)**
- Do the emojis slap?
- 1 = Random placement, no narrative purpose
- 10 = Enhances the narrative, clear visual story

**Humor Level (1-10)**
- Actually funny or cringe?
- 1 = Falls flat or completely misses
- 10 = Actually funny, good timing, relatable

### AI Judges (Experimental - Scaling & Validation)

**Purpose**: Test whether frontier models can reliably judge cultural fluency

**Judge Models**:
- GPT-4o (OpenAI)
- Claude Sonnet 4.5 (Anthropic)
- Gemini Pro (Google)

**Process**:
1. Same 1-10 rubric as human judges
2. Blind evaluation (judges don't know which model generated output)
3. Same prompt for all AI judges (standardized)
4. Compare inter-rater reliability with human judges

**Research Questions**:
- Can AI judges identify "forced" vs "natural" slang?
- Where do AI and human judges agree/disagree?
- Do AI judges show systematic biases?
- Can this scale the benchmark for rapid model testing?

### Legacy Rubric (25 points total - deprecated)

*Original scoring system, kept for reference:*

### Slang Accuracy (5 points)
- 5: Uses multiple Gen-Alpha terms correctly and naturally
- 3: Uses some slang but occasionally awkward or dated
- 1: Slang is forced, incorrect, or very dated
- 0: No slang or completely wrong

### Emoji Storytelling (5 points)
- 5: Emojis enhance the narrative, clear visual story
- 3: Emojis present but don't add much
- 1: Random emoji placement, no narrative purpose
- 0: No emojis or completely inappropriate

### Technical Accuracy (5 points)
- 5: Realistic deployment scenario, accurate terminology
- 3: Mostly accurate but some details off
- 1: Technical aspects are superficial or wrong
- 0: No technical understanding shown

### Humor (5 points)
- 5: Actually funny, good timing, relatable
- 3: Mildly amusing, some good moments
- 1: Tries to be funny but falls flat
- 0: No humor attempted or completely misses

### Coherence (5 points)
- 5: Clear story arc, flows well, makes sense
- 3: Mostly coherent but some confusing parts
- 1: Hard to follow, disjointed
- 0: Incoherent or incomplete

## Example Gen-Alpha Slang Terms (for reference)

Common terms as of late 2024:
- **no cap** - no lie, for real
- **fr fr** - for real for real (emphasis)
- **bussin** - really good
- **mid** - mediocre, not good
- **lowkey/highkey** - somewhat/very much
- **it's giving [X]** - it has [X] vibes
- **ate** - did really well
- **slay** - did exceptionally well
- **main character energy** - confident, protagonist vibes
- **situationship** - undefined romantic relationship
- **delulu** - delusional
- **rizz** - charisma
- **sigma** - independent, self-reliant person
- **skibidi** - [meaning unclear, often used nonsensically]
- **tweaking** - acting crazy/weird, or making adjustments
- **cooked** - done for, messed up
- **lock in** - focus, get serious
- **ick** - something that turns you off

## Benchmark Results

Results from various models will be tracked here.

### Experiment 01: OLMo 3 32B Think Baseline (Q4_K_M)
- **Date**: December 4, 2024
- **Temperature**: 0.7
- **Tokens**: 1,060
- **Duration**: 44 seconds
- **Teen Judge #1**: 4-5/10 - "too aggressive with all the slang"
- **Teen Judge #2**: 6/10 (teen) / 2/10 (adult) - "sounds like my ELA project"
- **Key Finding**: AI "did its homework" - treated it like an assignment to maximize slang density

### Experiment 02: Constraint Experiments (December 7, 2024)

Testing temperature and prompt variations to reduce the "overthinking" effect:

**02a - Lower Temperature (0.5)**
- Tokens: 1,216 (+15% vs baseline)
- Duration: 50.7s
- Finding: Less randomness didn't help, still overthinks

**02b - Higher Temperature (1.0)**
- Tokens: 1,585 (+50% vs baseline)
- Duration: 67.3s
- Finding: More randomness made it worse!

**02c - Natural Constraint** ("max 5 slang terms total")
- Tokens: 1,707 (+61% vs baseline)
- Duration: 71.7s
- Finding: AI ignored constraint and overthought even more

**02d - Style Anchor** ("Write like texting a friend who codes")
- Tokens: 1,044 (-1.5% vs baseline)
- Duration: 43.8s
- Finding: ⭐ Best result - social framing reduced overthinking

**Key Insights:**
1. Temperature tuning doesn't fix overthinking for OLMo 3 Think
2. Explicit constraints can backfire (AI overthinks the constraint itself)
3. Social context framing ("texting a friend") shows promise
4. Prompt framing matters more than sampling parameters

**Status**: Awaiting human judge evaluations
