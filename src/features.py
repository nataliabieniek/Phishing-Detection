"""Feature extraction for phishing email detection.

Each function below computes ONE feature (or a group of related features)
for a single email record (dict with keys: sender, receiver, date, subject,
body, urls, label). Fill in the TODOs. Keep functions pure (no side
effects) so they are easy to test and vectorize with pandas.

Run this file directly to build data/features.csv from data/emails.json.
"""
import json
import re
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
EMAILS_PATH = ROOT / "data" / "emails.json"
FEATURES_PATH = ROOT / "data" / "features.csv"

# Keywords typically used to lure victims in phishing emails.
KEYWORDS = [
    "urgent", "verify", "suspended", "password", "click here", "account",
    "confirm", "security", "update", "login", "limited time", "act now",
]


# ---------------------------------------------------------------------------
# 1. Basic length-based features
# ---------------------------------------------------------------------------
def body_length(email: dict) -> int:
    """Number of characters in the email body."""
    # TODO: return len(email["body"])
    raise NotImplementedError


def word_count(email: dict) -> int:
    """Number of whitespace-separated words in the body."""
    # TODO: split email["body"] on whitespace and count tokens
    raise NotImplementedError


def avg_word_length(email: dict) -> float:
    """Average word length in the body (0 if there are no words)."""
    # TODO: use word_count / character count of words (exclude spaces)
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 2. Punctuation / formatting features
# ---------------------------------------------------------------------------
def dot_count(email: dict) -> int:
    """Number of '.' characters in the body."""
    # TODO: count occurrences of "." in email["body"]
    raise NotImplementedError


def exclamation_count(email: dict) -> int:
    """Number of '!' characters in the body."""
    # TODO: count occurrences of "!" in email["body"]
    raise NotImplementedError


def uppercase_ratio(email: dict) -> float:
    """Fraction of letters in the body that are uppercase."""
    # TODO: count uppercase letters / total letters
    raise NotImplementedError


def digit_count(email: dict) -> int:
    """Number of digit characters in the body."""
    # TODO: count characters matching \d in email["body"]
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 3. Keyword-based features
# ---------------------------------------------------------------------------
def keyword_count(email: dict, keywords: list = KEYWORDS) -> int:
    """Total number of (case-insensitive) keyword occurrences in the body."""
    # TODO: lowercase the body and sum occurrences of each keyword
    raise NotImplementedError


def has_keyword(email: dict, keyword: str) -> int:
    """1 if `keyword` appears (case-insensitive) in the body, else 0."""
    # TODO: return 1 if keyword.lower() in email["body"].lower() else 0
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 4. URL-based features
# ---------------------------------------------------------------------------
URL_RE = re.compile(r"(https?://\S+|www\.\S+)", re.IGNORECASE)


def url_count(email: dict) -> int:
    """Number of URLs found in the body (via regex)."""
    # TODO: return len(URL_RE.findall(email["body"]))
    raise NotImplementedError


def url_has_ip(email: dict) -> int:
    """1 if any URL in the body uses a raw IP address instead of a domain."""
    # TODO: for each URL matched, check with a regex like r"\d{1,3}(\.\d{1,3}){3}"
    raise NotImplementedError


# ---------------------------------------------------------------------------
# 5. TF-IDF features (computed over the whole corpus, not a single email)
# ---------------------------------------------------------------------------
def build_tfidf_matrix(bodies: list, max_features: int = 500):
    """Fit a TfidfVectorizer on all email bodies and return (matrix, vectorizer).

    TODO:
        from sklearn.feature_extraction.text import TfidfVectorizer
        vectorizer = TfidfVectorizer(max_features=max_features, stop_words="english")
        matrix = vectorizer.fit_transform(bodies)
        return matrix, vectorizer
    """
    raise NotImplementedError


# ---------------------------------------------------------------------------
# Orchestration: build a feature table for the whole dataset
# ---------------------------------------------------------------------------
SIMPLE_FEATURES = {
    "body_length": body_length,
    "word_count": word_count,
    "avg_word_length": avg_word_length,
    "dot_count": dot_count,
    "exclamation_count": exclamation_count,
    "uppercase_ratio": uppercase_ratio,
    "digit_count": digit_count,
    "keyword_count": keyword_count,
    "url_count": url_count,
    "url_has_ip": url_has_ip,
}


def build_feature_table(emails: list) -> pd.DataFrame:
    rows = []
    for email in emails:
        row = {"label": email["label"]}
        for name, fn in SIMPLE_FEATURES.items():
            row[name] = fn(email)
        rows.append(row)
    df = pd.DataFrame(rows)

    # TODO: append TF-IDF columns using build_tfidf_matrix([e["body"] for e in emails])
    #       e.g. tfidf_matrix, vectorizer = build_tfidf_matrix(...)
    #       tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    #       df = pd.concat([df, tfidf_df], axis=1)

    return df

def main():
    emails = json.loads(EMAILS_PATH.read_text(encoding="utf-8"))
    df = build_feature_table(emails)
    df.to_csv(FEATURES_PATH, index=False)
    print(f"Saved {len(df)} rows x {len(df.columns)} columns to {FEATURES_PATH}")


if __name__ == "__main__":
    main()
