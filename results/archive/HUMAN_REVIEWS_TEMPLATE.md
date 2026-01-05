# Human Reviews - Data Entry Template

After your kids complete the review sheets, enter their responses here.
This file will be read by `05_combined_analysis.py` to compare AI vs human scores.

## Instructions

1. Share `teen_review_top2_comparison.md` with your kids
2. They pick which one feels more natural
3. Enter their choice and comments below
4. Re-run `python experiments/05_combined_analysis.py`

---

## Reviewer Information

**Number of reviewers:** _____

**Reviewer profiles:**
- Reviewer 1: Age ____, Role (e.g., "Your son")
- Reviewer 2: Age ____, Role (e.g., "Your daughter")
- Reviewer 3: (if applicable)

---

## Top 2 Comparison Results

**Date reviewed:** ___________

### Which felt more natural?

**Reviewer 1:**
- [ ] Story A
- [ ] Story B
- [ ] Tie / Can't decide

**Comments (optional):**
```
[Their notes here]
```

---

**Reviewer 2:**
- [ ] Story A
- [ ] Story B
- [ ] Tie / Can't decide

**Comments (optional):**
```
[Their notes here]
```

---

## Full Ranking Results (Optional)

If your kids rated all 5 experiments:

### Reviewer 1 Scores (1-10)

- **Baseline (Temp 0.7)**: _____/10
- **Lower Temp (0.5)**: _____/10
- **Higher Temp (1.0)**: _____/10
- **Natural Constraint**: _____/10
- **Style Anchor**: _____/10

**Top 3 (ranked):**
1. _________________
2. _________________
3. _________________

---

### Reviewer 2 Scores (1-10)

- **Baseline (Temp 0.7)**: _____/10
- **Lower Temp (0.5)**: _____/10
- **Higher Temp (1.0)**: _____/10
- **Natural Constraint**: _____/10
- **Style Anchor**: _____/10

**Top 3 (ranked):**
1. _________________
2. _________________
3. _________________

---

## Overall Observations

**What stood out to them?**
```
[Any interesting patterns or reactions they mentioned]
```

**Did they find the task annoying or interesting?**
```
[Gauge their engagement - this determines if we can ask again]
```

**Agreement level between reviewers:**
- [ ] High (picked same winners)
- [ ] Medium (some overlap)
- [ ] Low (completely different)

---

## For Analysis Script

This section will be populated automatically when you run the analysis:

**AI Judge Rankings:**
1. (Will be filled by script)
2. ...

**Human Judge Rankings:**
1. (Will be calculated from above)
2. ...

**Correlation Score:** _____ (Will be calculated)

**Agreement Level:**
- [ ] Strong (>0.7) - Trust AI judges going forward
- [ ] Moderate (0.4-0.7) - Need more validation
- [ ] Weak (<0.4) - AI judges unreliable

---

## Next Steps Based on Results

**If agreement is strong:**
→ Use AI judges as primary, spot-check with humans quarterly
→ Blog post: "AI Judges Pass the Vibe Check"

**If agreement is weak:**
→ Fall back to expert analysis (you)
→ Blog post: "Why AI Can't Judge Cultural Fluency"
→ Valuable negative result!
