# Qwen/Qwen3.5-2B Fine-Tuning Datasets

This repository is dedicated to generating high-quality, large-scale synthetic coding datasets for fine-tuning Large Language Models, particularly the Qwen/Qwen3.5-2B model.

All datasets strictly follow the English ChatML JSONL format, making them instantly ready for use in popular finetuning frameworks.

## 🚀 Features
- **Massive Scale**: Datasets span tens of thousands of examples (15K+ and 40K+).
- **Absolute Uniqueness**: Every prompt and example is strictly unique. We use combinatorial approaches and sets to guarantee 0% repetition.
- **Multi-Topic**: Coverage includes Python, SQL, JS logic, and HTML/CSS/JS frontend building.
- **Automated Generation**: All datasets are generated using Python automation scripts.

## 📁 Datasets

### 1. General Coding Dataset (`qwen_coding_dataset.jsonl`)
- **Size**: 15,000 unique examples
- **Topics**: Python algorithms, SQL queries, JavaScript data manipulation
- **Script**: `dataset_builder.py`

### 2. Frontend Coding Dataset (`frontend_dataset.jsonl`)
- **Size**: 40,000 unique examples
- **Topics**: HTML structure, CSS styling, vanilla JavaScript interactions
- **Script**: `frontend_dataset_builder.py`

## 🛠️ How to Generate
If you need to regenerate the datasets or modify the parameters, simply execute the builder scripts:

```bash
# Generate the General Coding Dataset (15,000 examples)
python3 dataset_builder.py

# Generate the Frontend Dataset (40,000 examples)
python3 frontend_dataset_builder.py
```
