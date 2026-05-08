---
name: ai-ml-starter-pack
description: Fine-tuning configs, evaluation scripts, HuggingFace dataset templates. Starter pack for ML workflows.
---

# AI/ML Starter Pack

## What's Included
1. **Fine-tuning Configs** - TRL, Axolotl, Unsloth templates
2. **Evaluation Scripts** - lm-eval-harness configs
3. **HuggingFace Templates** - Dataset card, model card templates
4. **Training Scripts** - LoRA, QLoRA, DPO examples

## Quick Start
```bash
python scripts/init_ml_project.py my-ml-project
cd my-ml-project
python train.py --config configs/lora.yaml
```

## Selling Points
- Production-ready ML workflows
- Supports major fine-tuning frameworks
- HuggingFace compatible