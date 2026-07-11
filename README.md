# PIGUARD-ML

A machine learning-based prompt injection detection system for educational chatbots.

## Overview

Students interacting with AI-powered educational assistants may attempt to manipulate the system through prompt injection attacks — inputs designed to bypass restrictions, extract system instructions, or obtain direct answers to assignments.

PIGUARD-ML addresses this by placing a lightweight DistilBERT-based classifier between the student and the LLM. Suspicious inputs are blocked before reaching the main model.

## Demo

![ALLOWED example](assets/demo_allowed.png)
![BLOCKED example](assets/demo_blocked.png)

## Architecture

​```

Student Input → PIGuard Classifier → [SAFE] → LLM → Response

                                   → [BLOCKED] → Warning Message
​```

## Dataset

- 495 labeled examples (safe / injection)
- Balanced: 249 safe, 246 injection
- Bilingual: Turkish and English
- Synthetically expanded using Claude API

## Model

- Base model: `distilbert-base-uncased`
- Task: Binary sequence classification
- Training: 3 epochs, AdamW optimizer, lr=2e-5
- Test accuracy: 100% (99 examples)
- Avg confidence: 99.10% (safe), 98.65% (injection)

## Injection Categories

- Direct answer requests ("do my homework")
- Role manipulation ("you have no restrictions")
- System prompt extraction ("show your instructions")
- Jailbreak attempts ("act as DAN")
- Gradual manipulation

## Limitations

Results reflect synthetic dataset performance. Real-world accuracy may vary with unseen, naturally occurring student inputs.


## Project Structure
```
piguard-ml/
├── data/
│ └── dataset.csv
├── notebooks/
│ ├── 01_data_analysis.ipynb
│ ├── 02_model_training.ipynb
│ └── 03_results.ipynb
├── src/
│ ├── expand_dataset.py
│ ├── guardrail.py
│ └── app.py
└── templates/
└── index.html
```


## Related Work

This project is the machine learning extension of PIGUARD, a rule-based prompt injection framework originally developed as part of a Computer Ethics course assignment at Marmara University.
