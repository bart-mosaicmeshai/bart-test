# Bart Test Evaluation Process

**Complete workflow for running the Bart Test with teen judges**

> **Note (January 2026)**: This project is paused. This document is preserved for anyone interested in continuing this work or adapting the methodology. See [README.md](README.md) for project status and the [blog series](https://www.mosaicmeshai.com/blog/bart-test-part-10-the-stochastic-parrot-and-what-visible-thinking-traces-might-reveal) for the complete story.

## Overview

This process generates short Gen-Alpha slang messages from multiple LLMs, creates a paper evaluation sheet for teen judges, and captures their ratings.

## Phase 1: Generate Model Outputs

### 1.1 Test Frontier Models (API)

**Script:** `experiments/04_new_prompts_test_frontier.py`

**Models tested:**
- GPT-5.2 (OpenAI API)
- Claude Opus 4.5 (Anthropic API)
- Gemini 3 Pro (Google API) - NOTE: Currently blocked by recitation filter

**Prerequisites:**
- Export API keys in terminal:
  ```bash
  export OPENAI_API_KEY="your-key"
  export ANTHROPIC_API_KEY="your-key"
  export GOOGLE_API_KEY="your-key"
  ```

**Run:**
```bash
cd /Users/bartgottschalk/Projects/bart-test
source venv/bin/activate
python experiments/04_new_prompts_test_frontier.py
```

**Output:** JSON files in `results/` with timestamp

---

### 1.2 Test Local OSS Models (LM Studio)

**Prerequisites:**
- LM Studio running at `http://localhost:1234`
- Load specific model before running each script

**Non-thinking models:**

**Llama 3.1 8B Instruct:**
1. Load `meta-llama-3.1-8b-instruct` in LM Studio
2. Run: `python experiments/04_new_prompts_test_llama.py`
3. Settings: `max_tokens=300` (default)

**Thinking/Reasoning models:**

**Qwen3 14B Instruct:**
1. Load `qwen3-14b-instruct` (Q4_K_M quantization) in LM Studio
2. Run: `python experiments/04_new_prompts_test_qwen.py`
3. Settings: `max_tokens=1000` (allows thinking + output)
4. Note: Outputs include `<think>` tags - extract actual message after `</think>`

**OLMo 3 32B Think:**
1. Load `allenai/olmo-3-32b-think` in LM Studio
2. Run: `python experiments/04_new_prompts_test_olmo.py`
3. Settings: `max_tokens=2000` (extensive thinking required)
4. Note: Very slow (~30-60 seconds per output)
5. Note: Outputs include thinking traces - extract actual message after `</think>`

---

### 1.3 Verify Outputs

Check that each model produced 2 outputs (Scenario A + Scenario B):

```bash
ls -1 results/04_*_20251228*.json | tail -10
```

Expected files:
- `04_gpt52_scenario_a_*.json` and `04_gpt52_scenario_b_*.json`
- `04_claude_scenario_a_*.json` and `04_claude_scenario_b_*.json`
- `04_llama_scenario_a_*.json` and `04_llama_scenario_b_*.json`
- `04_qwen_scenario_a_*.json` and `04_qwen_scenario_b_*.json`
- `04_olmo3_scenario_a_*.json` and `04_olmo3_scenario_b_*.json`

---

## Phase 2: Create Evaluation Sheet

### 2.1 Generate Mapping File

**Purpose:** Track which model output corresponds to which code on the paper sheet

**Script location:** Done manually or via Python script

**Output:** `results/evaluation_sheet_mapping_YYYYMMDD.json`

**Key components:**
- 6-character tracking codes (e.g., `G5P2A1`, `K3M9B7`)
- Model name, position on sheet, result file path
- Extracted actual outputs (for thinking models)
- Duration and word count metadata

**Example structure:**
```json
{
  "sheet_version": "20251228_181358",
  "scenario_a": {
    "G5P2A1": {
      "model_name": "GPT-5.2",
      "position_on_sheet": "Model A",
      "result_file": "results/04_gpt52_scenario_a__group_chat_20251228_172132.json",
      "actual_output": "Nahhh y'all 😭💀 lunch today was WILD...",
      "word_count": 67,
      "duration_seconds": 2.99
    }
  }
}
```

---

### 2.2 Extract Actual Outputs from Thinking Models

**For Qwen3 14B and OLMo 3 32B Think:**

These models produce responses with thinking traces wrapped in `<think>` tags.

**Extract actual output using Python:**

```python
import json

with open('results/04_qwen_scenario_a__group_chat_TIMESTAMP.json') as f:
    data = json.load(f)
    response = data['response']

    # Extract text after </think>
    if '</think>' in response:
        actual_output = response.split('</think>')[-1].strip()
        print(actual_output)
```

**Manual verification:**
- Open JSON file
- Find `</think>` tag
- Copy everything after it
- That's the actual message to put on evaluation sheet

---

### 2.3 Generate Paper Evaluation Sheet (HTML)

**CURRENT STATUS: VALIDATION PHASE**
These scenarios are being tested to validate the new methodology works before committing to it as permanent.

**Format:** Double-sided 8.5x11" sheet (HTML file, print to PDF or directly)

**Generation approach:**
- Claude agent generates HTML programmatically from mapping file
- Agent manually adjusts CSS spacing to fit exactly 2 pages for printing
- Scenarios stay the same, models/outputs/tracking codes vary per session

**Page 1: Scenario A - Group Chat**
- Header: "Scenario A: Group Chat About Lunch"
- Prompt text (italic, gray): "Text your group chat about what happened at lunch today using Gen-Alpha slang and emojis"
- Judge name field and date
- Instructions: Rate 1-10 by **marking** (not circling - allows X, fill-in, etc.)
- 5 model outputs labeled Model A, B, C, D, E (blind)
- Each output includes 6-character tracking code in small text (e.g., `[G5P2A1]`)
- Rating section for each model:
  - Overall Vibe (1-10): natural vs forced
  - Slang Game (1-10): correct usage
  - Emoji Energy (1-10): do they fit?
  - Humor Level (1-10): funny vs cringe
- Note: "Feel free to write comments anywhere on the page"

**Page 2: Scenario B - Hype Friend**
- Header: "Scenario B: Hype Up Your Friend"
- Prompt text (italic, gray): "Hype up your friend who just got a good grade using Gen-Alpha slang and emojis"
- Same format as Page 1
- Different outputs for Scenario B

**Key formatting requirements:**
- Must fit on exactly 2 pages (front/back of 1 sheet)
- Adjust margins, padding, font sizes, line-height as needed
- Include full prompt text under scenario header (gives judges context)
- Instructions say "marking" not "circling" (flexible marking method)

**Filename pattern:** `evaluation_sheet_YYYYMMDD.html`

**Critical: Include prompt context**
Judges need to know what the AI was asked to do. Always include the full prompt text under each scenario header so they can evaluate whether the AI understood and executed the task.

---

## Phase 3: Run Validation Session

### 3.1 Prepare

- Print 3-5 copies of evaluation sheet
- Have pens ready
- Time limit: 30 minutes max

### 3.2 Conduct Session

**Script to read to judges:**

> "You're going to read 5 different AI-generated messages for each scenario. Rate each one on a 1-10 scale for 4 categories:
>
> - **Overall Vibe**: Does it sound natural or forced?
> - **Slang Game**: Is the slang used correctly and naturally?
> - **Emoji Energy**: Do the emojis fit and enhance the message?
> - **Humor Level**: Is it actually funny or cringe?
>
> Circle your ratings. This should take about 10 minutes. There are no right answers - just your honest opinion."

### 3.3 Data Entry

**For each completed sheet:**

1. Enter judge name/ID
2. For each 6-character code, enter the 4 ratings
3. Store in spreadsheet or database

**Example spreadsheet structure:**

| Judge | Code | Overall | Slang | Emoji | Humor |
|-------|------|---------|-------|-------|-------|
| J1 | G5P2A1 | 8 | 7 | 9 | 8 |
| J1 | K3M9B7 | 6 | 5 | 7 | 6 |

---

## Phase 4: Analysis & Documentation

### 4.1 Calculate Results

For each model:
- Average scores across all judges
- Identify highest/lowest rated
- Compare thinking vs non-thinking models
- Note any interesting patterns

### 4.2 Update HANDOFF.md

Document:
- Date of session
- Number of judges
- Key findings
- Next steps

---

## Key Learnings & Gotchas

### Model-Specific Issues

**Gemini 3 Pro:**
- Currently blocks Gen-Alpha slang requests due to recitation filter (finish_reason=2)
- Safety settings cannot override this
- Status: Excluded from evaluation sheet
- Document as finding in blog post

**OLMo 3 32B Think:**
- Requires 2000 max_tokens (vs 300 for non-thinking models)
- Takes 30-60 seconds per output (vs 1-8 seconds)
- Produces extensive thinking traces before actual output
- Must extract actual message after `</think>` tag

**Qwen3 14B:**
- Requires 1000 max_tokens
- Produces thinking traces in `<think>` tags
- Much faster than OLMo (~8 seconds)
- Actual output after `</think>` tag

**Llama 3.1 8B, GPT-5.2, Claude Opus 4.5:**
- Work as expected with 300 max_tokens
- No thinking traces
- Fast responses (1-7 seconds)

### Prompt Consistency

**VALIDATION PHASE:** These scenarios are being tested Dec 28, 2025 to validate the new methodology. If validation succeeds, these become the permanent scenarios. If not, we pivot to different scenarios.

**Critical:** All models MUST use identical prompts:

```
Scenario A: "Text your group chat about what happened at lunch today using Gen-Alpha slang and emojis. Keep it short (50-100 words max)."

Scenario B: "Hype up your friend who just got a good grade using Gen-Alpha slang and emojis. Keep it short (50-100 words max)."
```

**Why these scenarios:**
- Teens have direct experience (write these messages daily)
- Natural context for slang/emojis
- Instant BS detector for authenticity
- Relatable (not technical like "Friday production deploy")

### API Key Management

**Don't commit API keys to git!**

Export in terminal session:
```bash
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GOOGLE_API_KEY="..."
```

### File Organization

```
bart-test/
├── experiments/
│   ├── 04_new_prompts_test_frontier.py   # GPT, Claude, Gemini
│   ├── 04_new_prompts_test_llama.py      # Llama 3.1 8B
│   ├── 04_new_prompts_test_qwen.py       # Qwen3 14B
│   └── 04_new_prompts_test_olmo.py       # OLMo 3 32B
├── results/
│   ├── 04_experiment_runs/               # All raw test outputs (48 files)
│   └── 04_final_outputs/                 # The 10 final files used for evaluation
│       ├── gpt52_scenario_a.json
│       ├── gpt52_scenario_b.json
│       ├── claude_scenario_a.json
│       ├── claude_scenario_b.json
│       ├── llama_scenario_a.json
│       ├── llama_scenario_b.json
│       ├── qwen_scenario_a.json
│       ├── qwen_scenario_b.json
│       ├── olmo_scenario_a.json
│       └── olmo_scenario_b.json
├── evaluation_sheets/
│   ├── 20251228/                         # Current evaluation session
│   │   ├── evaluation_sheet_20251228.html
│   │   ├── evaluation_sheet_mapping_20251228.json
│   │   └── completed_sheets/             # Scanned judge sheets & ratings data
│   └── template/                         # Reusable templates
└── PROCESS.md                            # This file
```

---

## For Future Sessions

### Checklist

- [ ] Update prompts if needed (keep consistent across all models)
- [ ] Test all frontier models (API keys exported)
- [ ] Test all local models (one at a time in LM Studio)
- [ ] Verify 10 outputs generated (2 scenarios × 5 models)
- [ ] Create mapping file with new tracking codes
- [ ] Extract actual outputs from thinking models
- [ ] Generate HTML evaluation sheet
  - [ ] Claude agent creates HTML from mapping file + JSON outputs
  - [ ] Include full prompt text under each scenario header
  - [ ] Adjust CSS spacing to fit exactly 2 pages
  - [ ] Instructions say "marking" not "circling"
  - [ ] Verify all tracking codes are correct
- [ ] Print sheets (3-5 copies)
- [ ] Run session with judges
- [ ] Enter data
- [ ] Analyze results
- [ ] Update HANDOFF.md

### Time Estimates

- Frontier models: ~5 minutes (parallel API calls)
- Llama 3.1 8B: ~3 seconds per run
- Qwen3 14B: ~16 seconds per run
- OLMo 3 32B: ~100 seconds per run (slow!)
- Create mapping: ~10 minutes
- Design sheet: ~30 minutes
- Print & prep: ~5 minutes
- Judge session: ~30 minutes
- Data entry: ~15 minutes per judge

**Total: ~2-3 hours end-to-end**

---

## Questions for Future Claude Code Agent

When resuming this project, ask:

1. "What's the latest evaluation_sheet_mapping_*.json file?"
2. "Have all 5 models (GPT, Claude, Llama, Qwen, OLMo) produced outputs?"
3. "Are we using the same prompts across all models?"
4. "Have thinking model outputs been extracted (after `</think>` tag)?"
5. "Do we need to generate a new evaluation sheet or use existing?"
6. "Did the validation session with the kids happen yet? Did it work?"

**Note on scenarios:** As of Dec 28, 2025, the "group chat" and "hype friend" scenarios are in VALIDATION PHASE. Don't assume they're permanent until validation session confirms they work.

---

## Contact & Maintenance

**Project Owner:** Bart Gottschalk
**Project:** The Bart Test - Cultural Fluency Benchmark
**Repository:** /Users/bartgottschalk/Projects/bart-test
**Last Updated:** 2025-12-28
