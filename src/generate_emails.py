"""Generate synthetic English emails (JSON) from URLs of the Kaggle
'Phishing Site URLs' dataset (columns: URL, Label = bad/good).

Bad URLs -> phishing templates, good URLs -> legitimate templates.
"""
import argparse
import json
import random
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent


def build_email(idx, row, tpl, rng):
    template = rng.choice(tpl["phishing" if row.Label == "bad" else "legitimate"])
    fields = {
        "url": row.URL,
        "brand": rng.choice(tpl["brands"]),
        "sender": rng.choice(tpl["senders"]),
    }
    return {
        "id": idx,
        "template_id": template["id"],
        "subject": template["subject"].format(**fields),
        "body": template["body"].format(**fields),
        "url": row.URL,
        "label": 1 if row.Label == "bad" else 0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--urls", default=str(ROOT / "data" / "phishing_site_urls.csv"))
    ap.add_argument("--templates", default=str(ROOT / "templates" / "email_templates.json"))
    ap.add_argument("--out", default=str(ROOT / "data" / "emails.json"))
    ap.add_argument("--n", type=int, default=200, help="emails per class")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()

    rng = random.Random(args.seed)
    tpl = json.loads(Path(args.templates).read_text(encoding="utf-8"))
    df = pd.read_csv(args.urls)

    parts = [g.sample(n=min(args.n, len(g)), random_state=args.seed) for _, g in df.groupby("Label")]
    sample = pd.concat(parts).sample(frac=1, random_state=args.seed)

    emails = [build_email(i, row, tpl, rng) for i, row in enumerate(sample.itertuples(index=False))]
    Path(args.out).write_text(json.dumps(emails, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Saved {len(emails)} emails to {args.out}")


if __name__ == "__main__":
    main()
