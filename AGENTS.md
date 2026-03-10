# AGENTS Instructions

Welcome! This repository is focused on creating massive, high-quality, synthetic coding datasets for fine-tuning Large Language Models, specifically the Qwen/Qwen3.5-2B model.

When working in this repository, you **must** strictly adhere to the following rules established by the user:

### 1. Dataset Generation Rules
* **Format:** All datasets MUST be formatted in **English ChatML JSONL** format.
  * Example: `{"messages": [{"role": "system", "content": "..."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}`
* **Topics & Scale:** Datasets are typically multi-topic (e.g., Python, SQL, JS) and massive in scale (10,000 to 40,000+ examples).
* **ABSOLUTE UNIQUENESS:** There is a **strict, non-negotiable rule**: THERE MUST BE ABSOLUTELY NO REPETITIONS. Every single prompt and example must be 100% unique. Use mathematical combinatorics (`itertools`, random permutations) and a `seen_prompts` Set to enforce this.
* **Automation:** ALWAYS write Python automation scripts (e.g., `dataset_builder.py`) to generate the datasets. Do not try to write the JSONL files manually.

### 2. Repository Rules
* **Track Datasets:** DO NOT add `.jsonl` files to `.gitignore`. The user explicitly requires the generated datasets to be tracked and committed to the repository, regardless of their massive size.
* **Keep Scripts Runnable:** Ensure the generation scripts are well-structured, error-free, and can be executed via `python3 <script_name>.py` to instantly regenerate or expand the datasets.
