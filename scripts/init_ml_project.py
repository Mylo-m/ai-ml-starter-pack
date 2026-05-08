#!/usr/bin/env python3
"""
Initialize ML project with proper structure.
"""
import os
import sys

def init_ml_project(project_name):
    dirs = [
        f"{project_name}/configs",
        f"{project_name}/data",
        f"{project_name}/scripts",
        f"{project_name}/outputs"
    ]
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        # Create .gitkeep to track empty dirs
        open(os.path.join(d, ".gitkeep"), "w").close()
    
    # Create sample training script
    with open(f"{project_name}/train.py", "w") as f:
        f.write('''#!/usr/bin/env python3
import argparse
from transformers import TrainingArguments, Trainer
import yaml

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    
    with open(args.config) as f:
        config = yaml.safe_load(f)
    
    print(f"Training with config: {args.config}")
    print("Add your model/dataset loading here")
    # Your training code here

if __name__ == "__main__":
    main()
''')
    
    print(f"Created ML project: {project_name}")
    print(f"Next: cd {project_name} && python train.py --config configs/lora.yaml")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python init_ml_project.py <project_name>")
        sys.exit(1)
    init_ml_project(sys.argv[1])
