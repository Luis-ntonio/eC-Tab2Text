# eC-Tab2TExt: E-Commerce Attribute-Specific Review Generation

eC-Tab2TExt is a project focused on leveraging Large Language Models (LLMs) for generating attribute-specific product reviews from structured tabular data, particularly for the e-commerce domain. This repository contains all the necessary components, including dataset processing, model training, evaluation, and output generation.

## Table of Contents

- [Project Overview](#project-overview)
- [Repository Structure](#repository-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
  - [Dataset Preparation](#dataset-preparation)
  - [Model Training and Fine-tuning](#model-training-and-fine-tuning)
  - [Evaluation](#evaluation)
  - [Zero-Shot Testing](#zero-shot-testing)
- [Results and Outputs](#results-and-outputs)
- [Future Work](#future-work)
- [Contributing](#contributing)

---

## Project Overview

The project aims to address the gap in domain-specific datasets for e-commerce by introducing eC-Tab2TExt, a dataset tailored for attribute-specific text generation tasks. This dataset facilitates the transformation of structured product specifications into human-like reviews.

### Key Highlights

- **Dataset:** Structured tabular data sourced from e-commerce platforms.
- **Models:** Llama2-chat 7B, StructLM 7B, and Mistral_Instruct 7B.
- **Evaluation:** Metrics Bleu, Rouge-1, Rouge-L, BertScore, Fluency, Correctness and Faithfulness.
- **Applications:** Product reviews, scalable to other domains (e.g., healthcare, finance).

---

## Repository Structure

```
.
├── dictionaries       # Python scripts for handling keys and reviews
├── experiments        # Notebooks for training, testing, and evaluation
├── metrics            # Evaluation results for various models
├── Outputs            # Generated outputs and predictions
├── products           # Dataset files (raw, cleaned, formatted)
├── prompts            # JSON file containing prompts for text generation
├── scrapping          # Scripts for data scraping and preprocessing
├── urls               # URL data for product reviews and specifications
```

---

## Setup Instructions

### Prerequisites

- Python 3.10+
- Dependencies listed in `requirements.txt`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/eC-Tab2TExt.git
   cd eC-Tab2TExt
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Dataset Preparation

1. **Scrape product data**:
   ```bash
   python scrapping/scrap_products.py
   ```
2. **Clean and format data**:
   ```bash
   python scrapping/clean_products.py
   python scrapping/format_products.py
   ```

### Model Training and Fine-tuning

Train LLMs on the prepared dataset using the provided notebooks:
- `experiments/train_models.ipynb`

### Evaluation

Evaluate model outputs using:
- `experiments/evaluating_metrics.ipynb`

Metrics includes Bleu, Rouge-1, Rouge-L, BertScore, Fluency, Correctness and Faithfulness.

### Zero-Shot Testing

Run zero-shot evaluations for LLMs:
- `experiments/zero_shot_GPT.ipynb`
- `experiments/zero_shot_Gemini.ipynb`

---

## Results and Outputs

Evaluation results and outputs are stored in the following directories:
- `Outputs/` stores generated reviews for products.


---

## Future Work

- Expand the dataset to cover more e-commerce categories.
- Fine-tune models for domain-specific tasks in other industries (e.g., healthcare, finance).

---

## Contributing

Contributions are welcome! Please submit issues or pull requests for suggestions or improvements.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```

Feel free to let me know if there are additional elements you'd like to incorporate!
