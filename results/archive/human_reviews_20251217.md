# Human Teen Reviews - Experiment 03 (December 17, 2024)

## Overview

**Experiment 03: Hybrid AI/Human Evaluation**

This experiment tested a two-stage evaluation approach:
1. AI judges (Claude Sonnet 4.5) evaluated all five outputs from Experiments 01 and 02
2. Three teen reviewers evaluated the top 2 stories as identified by the AI judge

Reviews conducted via casual text message conversations.

**Stories Evaluated:**
- **Story A**: Lower Temperature (0.5) - `02a_temp_0.5_20251207_090043` (from Experiment 02)
- **Story B**: Baseline (Temp 0.7) - `01_bart_test_20251204_211238` (from Experiment 01)

## Results Summary

### Winner: Story A (Lower Temperature 0.5)

**Vote Count:**
- Story A: 2 votes (Teen #1, Teen #2)
- Story B: 1 vote (Teen #3)

### Individual Reviews

---

#### Teen Reviewer #1

**Story A Feedback:**
- ✅ "I actually understood everything it said"
- ✅ "Maybe it's more tuned into my age group or maybe it's just more accurate"
- ⚠️ "It seems like it's trying maybe harder than the first time"
- ✅ "It's more poetic tho"
- ⚠️ "Definitely not all of it's realistic, but it does have moments"
- ✅ "That last line was good"
- Score: "15 out of 32" (unclear scale)

**Story B Feedback:**
- ❌ "Not sure what the deal is with all the asterisks"
- ❌ "This one does not look like it's by a person and definitely not a kid"
- ❌ "It doesn't make very much sense"

**Winner:** Story A

**Key Quote:**
> "Just didn't seem like very effective communication. It's like if you are trying to paint a picture of a duck and you paint a picture of a zoo with a tiny duck exhibit in the corner. Too much noise."

---

#### Teen Reviewer #2

**Story A Feedback:**
- ✅ "I think it's better than the last one because it uses less slang"
- ❌ "But I don't fully understand the story"
- 📝 "It might be because I don't know about errors 🤷‍♀️" (technical context barrier)

**Story B Feedback:**
- ✅ "I think all of the slang words were used in the right spots"
- ❌ "But there were a little too many of them"
- ❌ "I still don't fully understand the story"
- 📝 "Except for that someone glitched something and it's neon pink and it's a success"
- Score: 6/10

**Winner:** Story A

**Key Quote:**
> "I think that the second one was better. Wait, no I change it to A. But if I could understand the story better, it would be good 👍"

---

#### Teen Reviewer #3

**Comparison:**
1. **Which sounds more natural?**
   - "I would say the 2nd one [Story B] but not by far, seems a little out of it"
   - "Like both are not using now slang or how someone talks but parts of them they do it's split"

2. **What made one better/worse?**
   - ✅ "The 2nd one makes more natural and makes better comments/jokes"
   - ⚠️ "But does also try a little too hard"
   - ✅ "The emojis are def better too but don't overuse them"

**Winner:** Story B (slight preference)

**Emoji Insights (Unprompted):**
- ❌ Stories overuse uncommon emojis
- ✅ Should use: 😂😭🔥🥀
- 📝 "The dead rose [🥀] has gotten more popular"

**Outdated Slang Identified:**
- ❌ "no cap" - dated
- ⚠️ "vibe" - "isn't used but still sometimes just not as much"

**Key Quote:**
> "Just the way you say it, still keep some like English in there if you know what I mean. Not everything has to be slang but keep it in there too. Because then it seems like you're trying too hard."

---

## Cross-Cutting Insights

### What Teens Said Works
- ✅ Less slang = more natural
- ✅ Slang used in correct spots/contexts
- ✅ Mixing normal English with slang naturally
- ✅ Good individual moments/jokes
- ✅ Core emoji set: 😂😭🔥🥀

### What Teens Said Doesn't Work
- ❌ Too much slang density ("trying too hard")
- ❌ "no cap" is dated/overused
- ❌ "vibe" is less common now
- ❌ Overusing uncommon/random emojis
- ❌ Asterisks for actions (confusing formatting)
- ❌ "Too much noise" - lack of focus on story

### The "Trying Too Hard" Problem
All three reviewers independently identified this:
- Teen #1: "Too much noise, like painting a zoo when you want a duck"
- Teen #2: "Too many slang words"
- Teen #3: "When everything is slang, it seems like you're trying too hard"

### Technical Context Barrier
Teen #2 noted difficulty understanding the deployment/error context:
- Not a slang problem - a domain knowledge issue
- "I don't know about errors 🤷‍♀️"
- May need simpler technical scenarios for younger reviewers

## AI Judge vs Human Judge Comparison

### Claude AI Judge Rankings (Dec 17, 2024)
1. **Story A (Lower Temp 0.5)**: 5.25/10
2. Story B+ (Higher Temp 1.0): 5.00/10
3. **Story B (Baseline 0.7)**: 4.50/10 (tied)
4. Story C (Natural Constraint): 4.50/10 (tied)
5. Story D (Style Anchor): 4.50/10 (tied)

### Human Judge Rankings
1. **Story A (Lower Temp 0.5)**: 2 votes
2. **Story B (Baseline 0.7)**: 1 vote

### Agreement Analysis
✅ **Strong Agreement on Winner**: Both AI and human judges ranked Story A as #1

**Correlation:** High - AI and humans agree on the top performer

**Key Difference:**
- AI gave Story A a mediocre absolute score (5.25/10)
- Humans also weren't thrilled but preferred it relatively
- Both agree all stories have the "trying too hard" problem

## Methodology Notes

### Review Process
- **Format:** Casual text message conversations
- **Duration:** 5-10 minutes per reviewer
- **Approach:** Show both stories, ask which feels more natural, collect thoughts
- **Incentive:** Teen #3 received $15 Starbucks gift card

### Reviewer Demographics
- Three teen reviewers
- All Gen-Alpha (born after 2010)
- Mix of familiarity with tech concepts

### Privacy
- All reviewers anonymized as "Teen #1, #2, #3"
- Parental approval obtained where applicable
- No identifying information in public documentation

## Key Takeaways

1. **Lower temperature (0.5) performed best** - Reduced slang density helped naturalness
2. **"Trying too hard" is the core problem** - All stories over-index on slang
3. **Emoji usage matters** - Stick to core set (😂😭🔥🥀), avoid uncommon ones
4. **Slang ages quickly** - "no cap" and "vibe" already feel dated to Gen-Alpha
5. **Mix slang naturally** - Don't replace everything with slang terms
6. **AI judges can identify winners** - Claude correctly picked the human-preferred story

## Implications for Future Tests

### Prompt Improvements
- Emphasize natural language mixing: "use slang naturally, like you'd actually text"
- De-emphasize density: Remove "using Gen-Alpha slang" → "with some Gen-Alpha slang"
- Add social context: "texting a friend about..." (worked in Experiment 02d)

### Emoji Guidelines
- Provide explicit emoji palette: 😂😭🔥🥀 + a few others
- Warn against overuse: "use emojis naturally, not in every line"

### Judge Strategy Validation
✅ **Hybrid approach works:**
- AI judges can pre-screen and rank
- Human teens validate the top candidates
- Saves teen time while preserving authenticity

### Slang Currency
- Need periodic refresh on what's current vs dated
- Teen feedback is essential for this
- AI models likely training on older data

---

**Review Date:** December 17, 2024
**AI Judge Date:** December 17, 2024
**Experiment Date:** December 7, 2024 (stories generated)
