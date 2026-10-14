# Phishing and Malicious URL Detection (TF-IDF + Naive Bayes / SVM)

## Structure
- `data/` – dataset (`phishing_site_urls.csv` from Kaggle, not committed) and generated `emails.json`
- `templates/email_templates.json` – English email templates (phishing / legitimate)
- `src/generate_emails.py` – builds emails from dataset URLs
- `Dockerfile`, `docker-compose.yml`, `requirements.txt`

## Usage
1. Download the dataset: https://www.kaggle.com/datasets/taruntiwarihp/phishing-site-urls and put `phishing_site_urls.csv` into `data/`.
2. Generate emails:
   - Docker: `docker compose run --rm app`
   - Locally: `pip install -r requirements.txt && python src/generate_emails.py --n 200`
3. Jupyter: `docker compose up jupyter` → http://localhost:8888

Output (`data/emails.json`): list of `{id, template_id, subject, body, url, label}` (1 = phishing, 0 = legitimate).
All brands are fictional ("Example ..."); data is synthetic and for detector training only.
