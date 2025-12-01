# LLM Fundamentals - Day 1-2: Parameter Experiments

A collection of experiments exploring how LLM generation parameters affect output quality, creativity, and consistency using Google's Gemini API.

## 📋 Overview

This project demonstrates the impact of key LLM parameters through practical experiments:
- **Temperature**: Controls determinism vs. creativity
- **top_p**: Nucleus sampling for output diversity
- **top_k**: Limiting candidate token selection
- **frequency_penalty**: Reducing word repetition
- **Prompt Quality**: Comparing vague, detailed, and structured prompts

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Google Gemini API key

### Installation

1. Clone or navigate to the project directory:
   ```bash
   cd e:\Annu_Learnings\LLMs_fundamentals\Day1-2
   ```

2. Install dependencies:
   ```bash
   pip install google-generativeai python-dotenv
   ```

3. Set up environment variables:
   - Copy `.env_example` to `.env`
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_actual_api_key_here
     ```

### Running Experiments

Execute any experiment script:
```bash
python temperature_exp.py
python top_p_exp.py
python top_k_exp.py
python prompt_quality_exp.py
```

## 📁 Project Structure

```
Day1-2/
├── .env_example           # Environment template
├── README.md              # This file
├── experiment_list.txt    # Experiment guidelines
├── temperature_exp.py     # Temperature parameter experiment
├── top_p_exp.py          # Top-p parameter experiment
├── top_k_exp.py          # Top-k parameter experiment
├── prompt_quality_exp.py # Prompt quality comparison
├── temperature_outputs/  # Generated outputs (auto-created)
├── top_p_outputs/        # Generated outputs (auto-created)
├── top_k_outputs/        # Generated outputs (auto-created)
└── prompt_quality_outputs/ # Generated outputs (auto-created)
```

## 🧪 Experiments

### Experiment 1: Temperature
**File**: `temperature_exp.py`

Explore how temperature affects output determinism:
- `0.1` → Deterministic, factual
- `0.7` → Balanced creativity
- `1.2` → Chaotic, unpredictable

### Experiment 2: Top-p (Nucleus Sampling)
**File**: `top_p_exp.py`

Control vocabulary range:
- `0.1` → Limited vocabulary
- `0.5` → Balanced selection
- `0.9` → Wide creative freedom

### Experiment 3: Top-k
**File**: `top_k_exp.py`

Restrict candidate tokens:
- `10` → Very limited
- `50` → Moderate
- `100` → Broad selection

### Experiment 4: Frequency Penalty
**File**: `prompt_quality_exp.py` (integrated)

Reduce word repetition by adjusting frequency penalties.

### Experiment 5: Prompt Quality
**File**: `prompt_quality_exp.py`

Compare three prompt types:
- **Vague**: Minimal instructions
- **Detailed**: Complete requirements
- **Structured**: Strict format requirements

## 📊 Output Files

Each experiment generates:
- Individual text files with responses
- `summary.json` with metadata (length, timestamps, errors)

Example structure:
```
temperature_outputs/
├── temp_0.1.txt
├── temp_0.7.txt
├── temp_1.2.txt
└── summary.json
```

## 🔐 Security Best Practices

- **Never commit `.env`** to version control
- Use `.env_example` as a template
- Keep API keys secure and rotate regularly
- Don't share `.env` files with unauthorized users

## 🛠️ Requirements

```
google-generativeai>=0.3.0
python-dotenv>=0.19.0
```

Install with:
```bash
pip install -r requirements.txt
```

## 📝 Notes

- All outputs are UTF-8 encoded
- Experiments use `gemini-2.5-flash` model
- Timestamps are recorded for each run
- Error handling logs issues to `summary.json`

## 🤝 Contributing

To add new experiments:
1. Follow the existing pattern
2. Create output directories automatically
3. Save results to JSON summary
4. Document in `experiment_list.txt`

## 📚 References

- [Google Gemini API Documentation](https://ai.google.dev/)
- [LLM Parameter Guide](https://ai.google.dev/api/rest)

---
