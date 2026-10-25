# Phishing and Malicious URL Detection (TF-IDF + Naive Bayes / SVM)

Projekt 3: wykrywanie ataków phishingowych i złośliwych URL-i za pomocą TF-IDF i Naive Bayes / SVM.
Cel: F1 > 0.92 przy FPR < 2%. Lista 200 cech: `docs/ProjektDzikieWilki.xlsx`.

## Structure
- `data/` – source datasets
  - `Nigerian_Fraud.csv`, `SpamAssasin.csv` – real emails (`sender, receiver, date, subject, body, urls, label`), from the Kaggle "Phishing Email Dataset"
  - `phishing_site_urls.csv` – URL list (`URL, Label` = bad/good), from Kaggle "Phishing Site URLs"
  - `emails.json`, `features.csv` – generated
- `results/features.xlsx` – generated feature table (`email_id`, all features, `label`)
- `docs/ProjektDzikieWilki.xlsx` – feature list with examples
- `src/main.py` – main entry point of the app (runs the pipeline stages)
- `src/build_dataset.py` – combines the two email datasets, keeps only emails with a URL, replaces the URL with one sampled from `phishing_site_urls.csv` (bad→phishing, good→legit), fills missing fields → `data/emails.json`
- `src/generate_emails.py` – generates synthetic emails from the URL dataset
- `src/features_main.py` – base features (length, punctuation, keywords, URLs, total length, TF-IDF) and the feature-table builder
- `src/features_klaudia.py` (67), `src/features_natalia.py` (68), `src/features_milena.py` (65) – phishing features from the Excel list, split between team members
- `Dockerfile`, `docker-compose.yml`, `requirements.txt`

## Local setup, step by step
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Run the whole pipeline (or a single stage):
   ```
   python src/main.py            # = all
   python src/main.py dataset    # -> data/emails.json
   python src/main.py features   # -> data/features.csv + results/features.xlsx
   ```
   - `data/emails.json`: list of `{sender, receiver, date, subject, body, urls, label}`, `label` is `"bad"` (phishing) or `"good"` (legitimate). Missing sender/receiver/subject/date are filled with a safe placeholder ("Jan Kowalski").
   - `data/features.csv` / `results/features.xlsx`: one row per email, columns = `email_id` + all features + `label`.
3. Implement the TODOs in `src/features_main.py` and in your own `src/features_<name>.py`.

## Writing features
- Each function takes one email record (dict) and returns `int` 0/1 (1 = feature present); base features return a count/ratio.
- Function name = column name in the results file. Keep functions pure (no side effects).
- Register a new feature in the `FEATURES` dict at the bottom of your file; `features_main.py` merges all of them.

All data is used for research/training a phishing detector only.
