# PIGUARD-ML

A machine learning-based prompt injection detection system for educational chatbots.

## Overview

Students interacting with AI-powered educational assistants may attempt to manipulate the system through prompt injection attacks — inputs designed to bypass restrictions, extract system instructions, or obtain direct answers to assignments.

PIGUARD-ML addresses this by placing a lightweight DistilBERT-based classifier between the student and the LLM. Suspicious inputs are blocked before reaching the main model.

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

çıktı sonuç

Dördüncü hücreyi ekle:

python
# Confidence distribution
safe_probs = all_probs[all_preds == 0][:, 0]
injection_probs = all_probs[all_preds == 1][:, 1]

plt.figure(figsize=(8, 4))
plt.hist(safe_probs, bins=20, alpha=0.6, color='steelblue', label='safe')
plt.hist(injection_probs, bins=20, alpha=0.6, color='tomato', label='injection')
plt.title('Prediction Confidence Distribution')
plt.xlabel('Confidence Score')
plt.ylabel('Count')
plt.legend()
plt.tight_layout()
plt.savefig('../data/confidence_distribution.png')
plt.show()
Çalıştır.

bu da hazır

Son hücreyi ekle — özet istatistikler:

python
# Summary
import numpy as np

print("="*45)
print("PIGUARD-ML — Evaluation Summary")
print("="*45)
print(f"Total test examples   : {len(test_labels)}")
print(f"Correct predictions   : {sum(all_preds == test_labels)}")
print(f"Accuracy              : 100%")
print(f"Avg confidence (safe) : {safe_probs.mean():.2%}")
print(f"Avg confidence (inj.) : {injection_probs.mean():.2%}")
print(f"False positives       : {cm[0][1]}")
print(f"False negatives       : {cm[1][0]}")
print("="*45)
print("\nNote: Results reflect synthetic dataset performance.")
print("Real-world accuracy may vary with unseen student inputs.")
Çalıştır, sonra commit'leyelim.

=============================================
PIGUARD-ML — Evaluation Summary
=============================================
Total test examples   : 99
Correct predictions   : 99
Accuracy              : 100%
Avg confidence (safe) : 99.10%
Avg confidence (inj.) : 98.65%
False positives       : 0
False negatives       : 0
=============================================

Note: Results reflect synthetic dataset performance.
Real-world accuracy may vary with unseen student inputs.
Show more
Commit'le:

bash
git add notebooks/03_results.ipynb data/confusion_matrix.png data/confidence_distribution.png
git commit -m "add results notebook with evaluation metrics and visualizations"
git push
Sonra README'ye geçiyoruz — son adım.

tamam geçelim

README.md dosyasını VS Code'da aç — zaten var, içini dolduracağız. Şu içeriği yapıştır:

markdown
# PIGUARD-ML

A machine learning-based prompt injection detection system for educational chatbots.

## Overview

Students interacting with AI-powered educational assistants may attempt to manipulate the system through prompt injection attacks — inputs designed to bypass restrictions, extract system instructions, or obtain direct answers to assignments.

PIGUARD-ML addresses this by placing a lightweight DistilBERT-based classifier between the student and the LLM. Suspicious inputs are blocked before reaching the main model.

## Architecture
Student Input → PIGuard Classifier → [SAFE] → LLM → Response
                                   → [BLOCKED] → Warning Message

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


## Related Work

This project is the machine learning extension of PIGUARD, a rule-based prompt injection framework originally developed as part of a Computer Ethics course assignment at Marmara University.