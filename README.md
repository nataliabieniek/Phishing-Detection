# Phishing and Malicious URL Detection (TF-IDF + Naive Bayes / SVM)

## Structure
- `data/` – source datasets 
  - `Nigerian_Fraud.csv`, `SpamAssasin.csv` – real emails (`sender, receiver, date, subject, body, urls, label`), from the Kaggle "Phishing Email Dataset"
  - `phishing_site_urls.csv` – URL list (`URL, Label` = bad/good), from Kaggle "Phishing Site URLs"
- `src/build_dataset.py` – combines the two email datasets, keeps only emails with a URL, replaces the URL with one sampled from `phishing_site_urls.csv` (bad→phishing, good→legit), fills missing fields → `data/emails.json`
- `src/features.py` – feature extraction (length, punctuation, keywords, URLs, TF-IDF) → `data/features.csv`
- `Dockerfile`, `docker-compose.yml`, `requirements.txt`

## Local setup, step by step
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Build the emails database:
   ```
   python src/build_dataset.py
   ```
   → `data/emails.json`: list of `{sender, receiver, date, subject, body, urls, label}`, `label` is `"bad"` (phishing) or `"good"` (legitimate). Missing sender/receiver/subject/date are filled with a safe placeholder ("Jan Kowalski").
3. Implement the TODOs in `src/features.py`, then build the feature table:
   ```
   python src/features.py
   ```
   → `data/features.csv`: one row per email, columns = extracted features + `label`.


All data is used for research/training a phishing detector only.
