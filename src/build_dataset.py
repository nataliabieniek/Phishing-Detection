"""Build the final emails dataset by combining Nigerian_Fraud.csv (phishing)
and SpamAssasin.csv (ham + phishing), keeping only emails that contain at
least one URL (urls == 1), and replacing every URL found in the body with a
URL sampled from phishing_site_urls.csv:
  - label == 1 (phishing)  -> a "bad"  URL
  - label == 0 (legitimate) -> a "good" URL

Missing sender/receiver/subject/date values are filled with safe placeholders
(a generic "Jan Kowalski" sender/receiver, "No subject", and today 08:00 in
the same RFC 2822 format as the source data).

Output: data/emails.json with records:
  sender, receiver, date, subject, body, urls, label (label is "bad"/"good")
"""
import argparse
import json
import re
from datetime import datetime
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
URL_RE = re.compile(r"(https?://\S+|www\.\S+)", re.IGNORECASE)

PLACEHOLDER_SENDER = "Jan Kowalski <jan.kowalski@example.com>"
PLACEHOLDER_RECEIVER = "jan.kowalski@example.com"
PLACEHOLDER_SUBJECT = "No subject"


def placeholder_date() -> str:
    """Today at 08:00:00, formatted like the source data, e.g.
    'Wed, 14 Oct 2026 08:00:00 -0700'."""
    return datetime.now().strftime("%a, %d %b %Y 08:00:00 -0700")


def fill_missing(df: pd.DataFrame) -> pd.DataFrame:
    df["sender"] = df["sender"].fillna(PLACEHOLDER_SENDER)
    df["receiver"] = df["receiver"].fillna(PLACEHOLDER_RECEIVER)
    df["subject"] = df["subject"].fillna(PLACEHOLDER_SUBJECT)
    df["date"] = df["date"].fillna(placeholder_date())
    return df


def load_source(path):
    df = pd.read_csv(path)
    df = df[df["urls"] == 1].copy()
    return fill_missing(df)


def pick_url_pool(url_csv):
    df = pd.read_csv(url_csv)
    bad = df.loc[df.Label == "bad", "URL"].tolist()
    good = df.loc[df.Label == "good", "URL"].tolist()
    return bad, good


def replace_urls(body, new_url):
    if not isinstance(body, str) or not URL_RE.search(body):
        return body, False
    return URL_RE.sub(new_url, body), True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nigerian", default=str(ROOT / "data" / "Nigerian_Fraud.csv"))
    ap.add_argument("--spamassasin", default=str(ROOT / "data" / "SpamAssasin.csv"))
    ap.add_argument("--urls", default=str(ROOT / "data" / "phishing_site_urls.csv"))
    ap.add_argument("--out", default=str(ROOT / "data" / "emails.json"))
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    nigerian = load_source(args.nigerian)
    spamassasin = load_source(args.spamassasin)
    combined = pd.concat([nigerian, spamassasin], ignore_index=True)
    combined = combined.sample(frac=1, random_state=args.seed).reset_index(drop=True)

    bad_urls, good_urls = pick_url_pool(args.urls)
    rng_bad = iter(pd.Series(bad_urls).sample(frac=1, random_state=args.seed, replace=True))
    rng_good = iter(pd.Series(good_urls).sample(frac=1, random_state=args.seed, replace=True))

    records = []
    for row in combined.itertuples(index=False):
        new_url = next(rng_bad) if row.label == 1 else next(rng_good)
        new_body, replaced = replace_urls(row.body, new_url)
        if not replaced:
            continue  # skip emails where no URL could be located despite urls==1
        records.append({
            "sender": row.sender,
            "receiver": row.receiver,
            "date": row.date,
            "subject": row.subject,
            "body": new_body,
            "urls": 1,
            "label": "bad" if row.label == 1 else "good",
        })

    Path(args.out).write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")
    n_phish = sum(r["label"] == "bad" for r in records)
    n_legit = sum(r["label"] == "good" for r in records)
    print(f"Saved {len(records)} emails to {args.out} (phishing={n_phish}, legit={n_legit})")


if __name__ == "__main__":
    main()
