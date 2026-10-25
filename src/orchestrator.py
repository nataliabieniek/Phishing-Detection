"""Orchestrator: sklada tabele cech ze wszystkich plikow features_*.py i zapisuje wyniki.

Kolumny: email_id (numer maila od 1), cechy bazowe, cechy Klaudii, Natalii,
Mileny, label. Zapis: results/features.csv i results/features.xlsx.
"""
import json
from pathlib import Path

import pandas as pd

import features_klaudia
import features_main
import features_milena
import features_natalia

ROOT = Path(__file__).resolve().parent.parent
EMAILS_PATH = ROOT / "data" / "emails.json"
RESULTS_DIR = ROOT / "results"
RESULTS_CSV = RESULTS_DIR / "features.csv"
RESULTS_XLSX = RESULTS_DIR / "features.xlsx"

ALL_FEATURES = {}
for module in (features_main, features_klaudia, features_natalia, features_milena):
    overlap = ALL_FEATURES.keys() & module.FEATURES.keys()
    if overlap:
        raise ValueError(f"Duplicate feature names in {module.__name__}: {sorted(overlap)}")
    ALL_FEATURES.update(module.FEATURES)


def build_feature_table(emails: list, with_tfidf: bool = False) -> pd.DataFrame:
    rows = []
    for i, email in enumerate(emails, start=1):
        row = {"email_id": i}
        for name, fn in ALL_FEATURES.items():
            row[name] = fn(email)
        row["label"] = email["label"]
        rows.append(row)
    df = pd.DataFrame(rows)

    if with_tfidf:
        matrix, vectorizer = features_main.build_tfidf_matrix([e["body"] for e in emails])
        names = ["tfidf_" + t for t in vectorizer.get_feature_names_out()]
        tfidf_df = pd.DataFrame(matrix.toarray(), columns=names)
        df = pd.concat([df.drop(columns="label"), tfidf_df, df["label"]], axis=1)
    return df


def run_features(with_tfidf: bool = False) -> pd.DataFrame:
    emails = json.loads(EMAILS_PATH.read_text(encoding="utf-8"))
    df = build_feature_table(emails, with_tfidf)
    RESULTS_DIR.mkdir(exist_ok=True)
    df.to_csv(RESULTS_CSV, index=False)
    df.to_excel(RESULTS_XLSX, index=False)
    print(f"Saved {len(df)} rows x {len(df.columns)} columns to {RESULTS_CSV} and {RESULTS_XLSX}")
    return df
