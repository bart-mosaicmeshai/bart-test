# OLMo 3 32B Think Experiments

Local experiments with Allen AI's OLMo 3 32B Think model - a fully open reasoning model with transparent training data and visible thinking traces.

## Hardware Setup

- **Machine**: Apple M4 Max, 128 GB unified memory, 16 cores
- **Inference**: LM Studio
- **Model**: `allenai/olmo-3-32b-think` (Q4_K_M quantization, 19.5 GB)

## Model Overview

OLMo 3 Think is a 32B parameter reasoning-focused model with:
- **65,536 token context window**
- **Transparent reasoning traces** - inspect intermediate thinking steps
- **Fully open** - training data (Dolma 3), code, and weights all available
- **Apache 2.0 license**

### Training Pipeline
1. Pre-trained on Dolma 3 (~5.9T tokens)
2. Supervised Fine-Tuning (SFT)
3. Direct Preference Optimization (DPO)
4. Reinforcement Learning with Verifiable Rewards (RLVR)

## Experiments

### Reasoning & Chain-of-Thought
- [ ] **Thinking Trace Analysis** - Extract and analyze intermediate reasoning traces
- [ ] **Reasoning Depth Control** - Test how token limits affect answer quality
- [ ] **Multi-step Math** - Benchmark on GSM8K, MATH datasets

### Comparative Studies
- [ ] **Think vs Instruct** - Compare reasoning quality between variants
- [ ] **7B vs 32B Think** - Find the complexity threshold where 7B breaks down
- [ ] **Open vs Closed** - Compare with GPT-4o, Claude on identical tasks

### Code & Technical
- [ ] **Code Generation** - HumanEval, MBPP with thinking trace analysis
- [ ] **Code Review** - Bug finding with visible reasoning
- [ ] **Multi-file Refactoring** - Test 65K context utilization

### Novel Research
- [ ] **Synthetic CoT Data** - Generate training data from reasoning traces
- [ ] **Self-Consistency** - Analyze reasoning path diversity across runs
- [ ] **Thinking Compression** - Achieve same quality with shorter traces
- [ ] **Adversarial Reasoning** - Prompts designed to mislead reasoning

### Practical Applications
- [ ] **Long Document Q&A** - Utilize full 65K context
- [ ] **Multi-turn Reasoning** - Complex problems with conversation memory
- [ ] **Tool Use Planning** - Test tool call planning with reasoning

## Quantization Options

| Quant | Size | Speed | Quality | Use Case |
|-------|------|-------|---------|----------|
| Q4_K_M | 19.5 GB | Fastest | Good | Development, iteration |
| Q6_K | 26.4 GB | Medium | Better | Balanced experiments |
| Q8_0 | 34.3 GB | Slower | Best | Final runs, publication |

## Project Structure

```
olmo-3-32b-think/
├── README.md
├── experiments/           # Experiment scripts and notebooks
├── prompts/              # Prompt templates and test cases
├── results/              # Experiment outputs and analysis
└── scripts/              # Utility scripts
```

## Resources

- [Model Card (Hugging Face)](https://huggingface.co/allenai/Olmo-3-32B-Think)
- [OLMo 3 Blog Post](https://allenai.org/blog/olmo3)
- [LM Studio Model Page](https://lmstudio.ai/models/allenai/olmo-3-32b-think)
- [GGUF Quantizations](https://huggingface.co/lmstudio-community/Olmo-3-32B-Think-GGUF)

## License

MIT
