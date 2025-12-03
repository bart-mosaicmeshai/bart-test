# OLMo 3 Reasoning Experiments

Local experiments with Allen AI's OLMo 3 32B Think model - a fully open reasoning model with transparent training data and visible thinking traces.

## Motivation

OLMo 3 is unique among frontier-class models: **everything is open** - training data (Dolma 3), training code, intermediate checkpoints, and final weights. This enables experiments impossible with closed models.

Simon Willison's [initial testing](https://simonwillison.net/2025/Nov/22/olmo-3/) revealed fascinating behavior: the model spent **14+ minutes generating 8,437 tokens** of reasoning for a simple SVG drawing task. This "overthinking" phenomenon is a key area of investigation.

## Hardware Setup

- **Machine**: Apple M4 Max, 128 GB unified memory, 16 cores
- **Inference**: LM Studio
- **Model**: `allenai/olmo-3-32b-think` (Q4_K_M quantization, 19.5 GB)

## Model Overview

OLMo 3 Think is a 32B parameter reasoning-focused model with:
- **65,536 token context window**
- **Transparent reasoning traces** - inspect intermediate thinking steps
- **Fully open** - training data (Dolma 3), code, and weights all available
- **6x token efficiency** - competitive with Qwen 3 32B using far less training data
- **Apache 2.0 license**

### Training Pipeline
1. Pre-trained on Dolma 3 (~5.9T tokens from 9.3T corpus)
2. Supervised Fine-Tuning (SFT)
3. Direct Preference Optimization (DPO)
4. Reinforcement Learning with Verifiable Rewards (RLVR)

## Experiments

### Overthinking Analysis ⭐ Priority
Inspired by Simon Willison's observations of excessive reasoning on simple tasks.

- [ ] **Reasoning Token Overhead** - Measure thinking tokens vs task complexity
- [ ] **Think vs Instruct on Simple Tasks** - When does reasoning hurt performance?
- [ ] **Reasoning Constraints** - Can we prompt "think briefly" effectively?
- [ ] **Creative Task Penalty** - Benchmark reasoning overhead on open-ended tasks

### Reasoning & Chain-of-Thought
- [ ] **Thinking Trace Analysis** - Extract and analyze intermediate reasoning traces
- [ ] **Reasoning Depth Control** - Test how token limits affect answer quality
- [ ] **Multi-step Math** - Benchmark on GSM8K, MATH datasets
- [ ] **Self-Consistency** - Analyze reasoning path diversity across runs

### Training Data Transparency
Unique experiments enabled by Dolma 3's openness.

- [ ] **OlmoTrace Investigation** - Trace outputs back to training data sources
- [ ] **Knowledge Attribution** - Find training data for correct vs incorrect answers
- [ ] **Training Gap Analysis** - Find knowledge gaps, test model on those topics
- [ ] **Data Poisoning Audit** - Security review of training data samples

### Comparative Studies
- [ ] **Think vs Instruct** - Compare reasoning quality between variants
- [ ] **7B vs 32B Think** - Find the complexity threshold where 7B breaks down
- [ ] **OLMo 3 vs Qwen 3 32B** - Test the 6x token efficiency claim
- [ ] **Open vs Closed** - Compare with GPT-4o, Claude on identical tasks

### Code & Technical
- [ ] **Code Generation** - HumanEval, MBPP with thinking trace analysis
- [ ] **Code Review** - Bug finding with visible reasoning
- [ ] **Multi-file Refactoring** - Test 65K context utilization

### Novel Research
- [ ] **Synthetic CoT Data** - Generate training data from reasoning traces
- [ ] **Thinking Compression** - Achieve same quality with shorter traces
- [ ] **Adversarial Reasoning** - Prompts designed to mislead reasoning

## Quantization Options

| Quant | Size | Speed | Quality | Use Case |
|-------|------|-------|---------|----------|
| Q4_K_M | 19.5 GB | Fastest | Good | Development, iteration |
| Q6_K | 26.4 GB | Medium | Better | Balanced experiments |
| Q8_0 | 34.3 GB | Slower | Best | Final runs, publication |

## Project Structure

```
olmo3-reasoning-experiments/
├── README.md
├── experiments/           # Experiment scripts and notebooks
├── prompts/              # Prompt templates and test cases
├── results/              # Experiment outputs and analysis
└── scripts/              # Utility scripts
```

## Resources

- [Model Card (Hugging Face)](https://huggingface.co/allenai/Olmo-3-32B-Think)
- [OLMo 3 Blog Post](https://allenai.org/blog/olmo3)
- [Simon Willison's Analysis](https://simonwillison.net/2025/Nov/22/olmo-3/)
- [LM Studio Model Page](https://lmstudio.ai/models/allenai/olmo-3-32b-think)
- [GGUF Quantizations](https://huggingface.co/lmstudio-community/Olmo-3-32B-Think-GGUF)
- [Dolma 3 Training Data](https://huggingface.co/datasets/allenai/dolma)
- [OlmoTrace Tool](https://olmotrace.allenai.org/)

## License

MIT
