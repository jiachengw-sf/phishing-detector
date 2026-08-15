# Phishing & Malicious URL Detector

My first machine learning project that classifies URLs as benign or malicious using lexical features extracted from the URL itself.

## Overview

This project trains a binary classifier on ~650,000 labeled URLs (Kaggle's Malicious URLs Dataset) to detect phishing links. They are grouped together as "malicious" vs. "benign."

## Dataset

- Source: [Kaggle Malicious URLs Dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset)
- ~651,191 URLs
- Original labels: benign, phishing, malware, defacement — combined into a binary label (0 = benign, 1 = malicious)

## Features

- URL length
- Special character count (`@`, `-`, `.`, `?`, `=`)
- Presence of a raw IP address instead of a domain
- Digit count
- Subdomain count
- Presence of suspicious keywords (login, verify, secure, account, etc.)
- Hyphen count
- Suspicious top-level domain (.tk, .ml, .ga, etc.)

## Model

- Random Forest Classifier with `class_weight='balanced'`
- Chosen over the default baseline because it prioritizes **recall** on malicious URLs over raw accuracy
    - *This is a more appropriate tradeoff for a security tool*
- **Results:** 83% accuracy, 0.80 recall / 0.72 precision on the malicious class

## Tech Stack

Python, pandas, scikit-learn, Streamlit, joblib

## Running Locally

1. Clone this repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run `02_data_processing.ipynb` → `03_model_training.ipynb` in order to regenerate `processed_urls.csv` and `phishing_model.pkl` (excluded from this repo due to file size)
4. Launch the app: `streamlit run app.py`

## Live Demo
(Coming Soon)