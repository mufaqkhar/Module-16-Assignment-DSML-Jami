# Diabetes Disease Progression Prediction — Simple Linear Regression

**Project status:** Proposal reviewed; baseline regression ready

## Overview
This Module 16 project investigates whether baseline body mass index (BMI) can predict diabetes disease progression one year later using simple linear regression.

## Dataset
The public diabetes regression dataset from scikit-learn contains 442 observations, 10 standardized baseline features, and a quantitative progression target. See `data/README.md` for attribution and loading details.

## Project scope
The assignment focuses on Git workflow, research proposal, commits, branching, and merge conflict resolution. A small runnable baseline is provided in `regression.py`.

## Reproduce
```bash
pip install -r requirements.txt
python regression.py
```

## Files
- `data/diabetes_bmi.csv`: BMI predictor and disease-progression target (442 rows)
- `proposal.md`: question, data provenance, and two-source literature scan
- `CONFLICT_NOTES.md`: actual conflict and manual resolution evidence
- `regression.py`: baseline linear regression example
