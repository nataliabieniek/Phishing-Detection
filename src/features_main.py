"""Cechy bazowe (wspolne) - dlugosci i interpunkcja.

Temat: Projekt 3 - Wykrywanie atakow phishingowych i zlosliwych URL-i za pomoca
TF-IDF i Naive Bayes / SVM. Cel: F1 > 0.92 przy FPR < 2%.

Kazda funkcja przyjmuje JEDEN rekord maila (dict z kluczami: sender, receiver,
date, subject, body, urls, label) i zwraca liczbe (int lub float) w formacie
podanym w docstringu. Nazwa funkcji = nazwa kolumny w results/features.csv.
Funkcje musza byc czyste (bez efektow ubocznych). Zostaw `return` w
narzuconym formacie - zmieniaj tylko logike wyznaczajaca `value`.

Skladanie tabeli i zapis wynikow: src/orchestrator.py.
Cechy z docs/ProjektDzikieWilki.xlsx: features_klaudia.py, features_natalia.py,
features_milena.py.
"""
# ---------------------------------------------------------------------------
# 1. Dlugosci
# ---------------------------------------------------------------------------
def body_length(email: dict) -> int:
    """Liczba znakow w tresci maila."""
    body = email.get("body", "")
    # TODO: value = len(body)
    value = 0
    return int(value)  # format zwrotu: int >= 0


def word_count(email: dict) -> int:
    """Liczba slow (rozdzielonych bialymi znakami) w tresci."""
    body = email.get("body", "")
    # TODO: value = len(body.split())
    value = 0
    return int(value)  # format zwrotu: int >= 0


def avg_word_length(email: dict) -> float:
    """Srednia dlugosc slowa w tresci (0.0 gdy brak slow)."""
    body = email.get("body", "")
    # TODO: suma dlugosci slow / liczba slow
    value = 0.0
    return round(float(value), 4)  # format zwrotu: float >= 0, 4 miejsca po przecinku


def total_length(email: dict) -> int:
    """Dlugosc calego maila: nadawca + odbiorca + data + temat + tresc."""
    # TODO: suma len(str(email.get(k, ""))) dla k w sender, receiver, date, subject, body
    value = 0
    return int(value)  # format zwrotu: int >= 0


# ---------------------------------------------------------------------------
# 2. Interpunkcja / formatowanie
# ---------------------------------------------------------------------------
def dot_count(email: dict) -> int:
    """Liczba znakow '.' w tresci."""
    body = email.get("body", "")
    # TODO: value = body.count(".")
    value = 0
    return int(value)  # format zwrotu: int >= 0


def exclamation_count(email: dict) -> int:
    """Liczba znakow '!' w tresci."""
    body = email.get("body", "")
    # TODO: value = body.count("!")
    value = 0
    return int(value)  # format zwrotu: int >= 0


def uppercase_ratio(email: dict) -> float:
    """Ulamek liter w tresci, ktore sa wielkie (0.0 gdy brak liter)."""
    body = email.get("body", "")
    # TODO: wielkie litery / wszystkie litery
    value = 0.0
    return round(float(value), 4)  # format zwrotu: float z zakresu 0-1, 4 miejsca po przecinku


def digit_count(email: dict) -> int:
    """Liczba cyfr w tresci."""
    body = email.get("body", "")
    # TODO: value = sum(c.isdigit() for c in body)
    value = 0
    return int(value)  # format zwrotu: int >= 0

# Cechy zwracane w tabeli (kolumna = klucz).
FEATURES = {
    "body_length": body_length,
    "word_count": word_count,
    "avg_word_length": avg_word_length,
    "total_length": total_length,
    "dot_count": dot_count,
    "exclamation_count": exclamation_count,
    "uppercase_ratio": uppercase_ratio,
    "digit_count": digit_count,
}


# ---------------------------------------------------------------------------
# 3. TF-IDF (liczone na calym korpusie, nie na pojedynczym mailu)
# ---------------------------------------------------------------------------
def build_tfidf_matrix(bodies: list, max_features: int = 500):
    """Dopasowuje TfidfVectorizer na wszystkich tresciach i zwraca (matrix, vectorizer)."""
    from sklearn.feature_extraction.text import TfidfVectorizer

    vectorizer = TfidfVectorizer(max_features=max_features, stop_words="english")
    matrix = vectorizer.fit_transform(bodies)
    return matrix, vectorizer
