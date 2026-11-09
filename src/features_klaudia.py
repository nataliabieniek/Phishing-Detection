"""Cechy phishingowe - Klaudia.

Zakres: cechy nr 1-67 z docs/ProjektDzikieWilki.xlsx (67 funkcji).

Kazda funkcja przyjmuje JEDEN rekord maila (dict z kluczami: sender, receiver,
date, subject, body, urls, label) i zwraca int 0/1 (1 = cecha wystepuje).
Nazwa funkcji = nazwa kolumny w results/features.xlsx.
Funkcje musza byc czyste (bez efektow ubocznych). Zostaw `return` w
narzuconym formacie - zmieniaj tylko logike wyznaczajaca `value`.
"""
import re


def _text(email: dict) -> str:
    """Temat + tresc maila, male litery."""
    return f"{email.get('subject', '')} {email.get('body', '')}".lower()


def _raw(email: dict) -> str:
    """Temat + tresc maila bez zmiany wielkosci liter."""
    return f"{email.get('subject', '')} {email.get('body', '')}"


def _match(text: str, patterns: list) -> int:
    """1 jesli ktorykolwiek wzorzec regex pasuje do `text`, inaczej 0."""
    return int(any(re.search(p, text) for p in patterns))


# URL ze schematem, z www. albo goly adres z popularna/podejrzana koncowka.
URL_RE = re.compile(
    r"(?:https?://|www\.)[^\s<>\"')\]]+"
    r"|\b(?:[a-z0-9-]+\.)+(?:com|net|org|info|biz|ru|cn|pl|de|uk|it|xyz|top|club|online|site|tk|ml|ga|cf|gq|cc|ws|pw|io|co|us|br|in|ly|gl|gd|me|at)"
    r"\b(?:/[^\s<>\"')\]]*)?",
    re.IGNORECASE,
)
IP_RE = re.compile(r"^\d{1,3}(?:\.\d{1,3}){3}$")

BRANDS = [
    "paypal", "microsoft", "google", "amazon", "apple", "facebook", "netflix",
    "outlook", "office", "linkedin", "instagram", "ebay", "yahoo", "dropbox",
    "wellsfargo", "chase", "citibank", "hsbc", "barclays", "santander", "allegro",
]
# Podmiany wizualne: rn->m, vv->w, cyfry zamiast liter.
HOMOGLYPHS = [("rn", "m"), ("vv", "w"), ("0", "o"), ("1", "l"), ("3", "e"), ("5", "s"), ("@", "a")]

UNUSUAL_TLDS = {
    "xyz", "top", "club", "online", "site", "info", "biz", "tk", "ml", "ga", "cf", "gq",
    "work", "click", "link", "loan", "win", "review", "country", "kim", "men", "date",
    "stream", "download", "racing", "bid", "trade", "party", "science", "zip", "mov",
    "buzz", "rest", "fit", "ws", "cc", "pw", "su", "ru", "cn",
}
SHORTENERS = {
    "bit.ly", "bitly.com", "tinyurl.com", "goo.gl", "t.co", "ow.ly", "is.gd", "buff.ly",
    "adf.ly", "tiny.cc", "rebrand.ly", "cutt.ly", "shorturl.at", "rb.gy", "t.ly", "s.id",
    "x.co", "lnkd.in", "db.tt", "qr.net", "tr.im", "v.gd", "bc.vc", "po.st",
}
# W zwyklym tekscie pomijamy marki bedace slowami ("apple"/"apply", "chase"/"phase").
TEXT_BRANDS = [b for b in BRANDS if b not in ("apple", "chase", "office", "ebay", "yahoo", "hsbc")]
GENERIC_ROLES = (
    r"(valued |dear |esteemed )?(customer|client|member|account ?holder|subscriber"
    r"|sir|madam|sir/madam|sir or madam|friend|beneficiary|partner)"
)


def _urls(email: dict) -> list:
    return URL_RE.findall(_raw(email))


def _host(url: str) -> str:
    host = re.sub(r"^[a-z]+://", "", url.lower())
    host = re.split(r"[/?#]", host, maxsplit=1)[0]
    host = host.rsplit("@", 1)[-1].split(":")[0]
    return host.strip(".")


def _hosts(email: dict) -> list:
    return [h for h in (_host(u) for u in _urls(email)) if "." in h]


def _sld(host: str) -> str:
    """Domena drugiego poziomu, np. 'paypal' dla 'login.paypal.com'."""
    parts = host.split(".")
    if len(parts) >= 3 and parts[-2] in ("co", "com", "org", "net", "gov", "ac"):
        return parts[-3]
    return parts[-2] if len(parts) >= 2 else host


def _one_edit(a: str, b: str) -> bool:
    """True jesli a i b roznia sie dokladnie jedna edycja (zamiana/wstawienie/usuniecie/przestawienie)."""
    if a == b or abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        diff = [i for i in range(len(a)) if a[i] != b[i]]
        if len(diff) == 1:
            return True
        return len(diff) == 2 and diff[1] == diff[0] + 1 and a[diff[0]] == b[diff[1]] and a[diff[1]] == b[diff[0]]
    short, long_ = (a, b) if len(a) < len(b) else (b, a)
    return any(long_[:i] + long_[i + 1:] == short for i in range(len(long_)))


def _deglyph(token: str) -> str:
    for src, dst in HOMOGLYPHS:
        token = token.replace(src, dst)
    return token


def _near_brand(token: str, brands: list = BRANDS) -> bool:
    """Token podszywa sie pod marke (literowka lub homoglif), ale nia nie jest."""
    if len(token) < 4 or token in brands:
        return False
    plain = _deglyph(token)
    for b in brands:
        if token.startswith(b) or token.endswith(b):
            continue  # "offices", "paypalsupport" to nie literowki
        if plain == b or _one_edit(token, b):
            return True
    return False


def urgency(email: dict) -> int:
    """Urgency. Przyklad: "You must verify your account within 24 hours or access will be suspended."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"\burgent(ly)?\b",
        r"\bimmediate(ly)?\b",
        r"as soon as possible|\basap\b",
        r"right away|without delay",
        r"act now|respond (now|promptly)",
        r"within \d+ (hours?|days?)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def time_pressure(email: dict) -> int:
    """Time Pressure. Przyklad: "This offer expires today."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"expires? (today|tonight|soon|in \d+)",
        r"(offer|deal|promotion) (ends|expires)",
        r"limited[- ]time",
        r"last chance",
        r"\bdeadline\b",
        r"only \d+ (hours?|days?) (left|remaining)",
        r"today only|before it'?s too late",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def threat_of_account_suspension(email: dict) -> int:
    """Threat of Account Suspension. Przyklad: "Your account will be disabled if you do not respond."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"account (will|may|could|has) (be |been )?(suspended|disabled|locked|closed|deactivated|terminated|blocked|frozen|restricted)",
        r"(suspend|lock|close|deactivate|disable|block|freeze|restrict) your account",
        r"account (suspension|deactivation|termination)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def threat_of_data_loss(email: dict) -> int:
    """Threat of Data Loss. Przyklad: "All your files will be deleted unless you verify ownership."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"(files|data|emails|messages|photos|documents|contacts) (will|may|could) (be )?(permanently )?(deleted|lost|removed|erased|destroyed)",
        r"permanently (deleted|lost|removed|erased)",
        r"lose (all )?(of )?your (data|files|emails|messages|photos|documents)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def threat_of_service_interruption(email: dict) -> int:
    """Threat of Service Interruption. Przyklad: "Your subscription will be terminated."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"(subscription|service|membership|mailbox|e-?mail account|access|plan) (will|may|could|has) (be |been )?(terminated|cancell?ed|interrupted|discontinued|suspended|stopped|expired)",
        r"service interruption",
        r"(lose|losing) access",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def security_alert_with_checking_pressure(email: dict) -> int:
    """Security Alert with checking pressure. Przyklad: "Suspicious activity has been detected on your account."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"(suspicious|unusual|unauthori[sz]ed|irregular) (activity|log ?in|sign[- ]?in|access|transaction|attempt)",
        r"security (alert|warning|notice|breach)",
        r"(someone|somebody) (tried|attempted) to (access|log|sign)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def immediately_account_recovery_request(email: dict) -> int:
    """Immediately Account Recovery Request. Przyklad: "Restore access to your account immediately."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"(restore|recover|reactivate|unlock|regain) (full )?(access to )?your account",
        r"account recovery",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def password_reset_request(email: dict) -> int:
    """Password Reset Request. Przyklad: "Reset your password using the link below."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"reset (your )?password",
        r"password reset",
        r"(change|update|renew) your password",
        r"password (has )?expire",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def credential_request(email: dict) -> int:
    """Credential Request. Przyklad: "Please enter your username and password."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"(enter|provide|confirm|verify|update|send|submit) (us )?(your )?(username|user name|login (details|credentials)|password|credentials|user ?id)",
        r"username and password",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def login_verification_request(email: dict) -> int:
    """Login Verification Request. Przyklad: "Log in to confirm your identity."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"(log ?in|sign ?in) (to|and) (confirm|verify|validate)",
        r"(confirm|verify|validate) your (identity|log ?in|account)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def repeated_login_prompt(email: dict) -> int:
    """Repeated Login Prompt. Przyklad: "Your session has expired, please log in again."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"session (has )?(expired|timed out)",
        r"(log|sign) ?in again",
        r"re-?(log|sign) ?in|re-?enter your (password|credentials)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def microsoft_login_redirect(email: dict) -> int:
    """Microsoft Login Redirect. Przyklad: "Continue by signing into Microsoft 365."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"(microsoft|office) ?365",
        r"microsoft account",
        r"sign ?in (to|with) (your )?(microsoft|outlook|office|onedrive)",
        r"\b(onedrive|sharepoint)\b",
        r"outlook (web|account|login)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def google_login_redirect(email: dict) -> int:
    """Google Login Redirect. Przyklad: "Sign in with your Google account."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"google account",
        r"sign ?in (to|with) (your )?(google|gmail)",
        r"gmail account|google drive|accounts\.google",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def bank_login_redirect(email: dict) -> int:
    """Bank Login Redirect. Przyklad: "Log in to your online banking account."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"(online|internet|mobile|e-?) ?banking",
        r"(log ?in|sign ?in) (to|into) your (bank|banking)",
        r"bank account (login|access)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_login_page(email: dict) -> int:
    """Fake Login Page. Przyklad: "Verify your account through our secure login page."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"secure (log ?in|sign[- ]?in|verification|account) (page|portal|link|form|server)",
        r"(log ?in|sign[- ]?in|verification) (page|portal|form)",
        r"click (here|the link|below|the button) to (log ?in|sign ?in|verify|confirm)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def personal_data_request(email: dict) -> int:
    """Personal Data Request. Przyklad: "Please confirm your personal information."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def pesel_request(email: dict) -> int:
    """PESEL Request. Przyklad: "Provide your PESEL number for verification."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def national_id_request(email: dict) -> int:
    """National ID Request. Przyklad: "Upload a copy of your identity document."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def passport_request(email: dict) -> int:
    """Passport Request. Przyklad: "Verify your passport information."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def birth_date_request(email: dict) -> int:
    """Birth Date Request. Przyklad: "Confirm your date of birth."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def address_request(email: dict) -> int:
    """Address Request. Przyklad: "Update your home address."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def phone_number_request(email: dict) -> int:
    """Phone Number Request. Przyklad: "Provide your mobile phone number."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def credit_card_request(email: dict) -> int:
    """Credit Card Request. Przyklad: "Confirm your credit card information."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def cvv_request(email: dict) -> int:
    """CVV Request. Przyklad: "Enter your card security code."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def pin_request(email: dict) -> int:
    """PIN Request. Przyklad: "Provide your card PIN."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def bank_account_request(email: dict) -> int:
    """Bank Account Request. Przyklad: "Verify your account number."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def security_question_request(email: dict) -> int:
    """Security Question Request. Przyklad: "Answer your account security question."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def document_upload_request(email: dict) -> int:
    """Document Upload Request. Przyklad: "Upload a copy of your ID document."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def misspelled_brand_name(email: dict) -> int:
    """Misspelled Brand Name. Przyklad: "Sign in to your Microsotf account."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def misspelled_domain(email: dict) -> int:
    """Misspelled Domain. Przyklad: "Visit paypaI-security.com."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def typosquatting_domain(email: dict) -> int:
    """Typosquatting Domain. Przyklad: "Access your account via rnicrosoft-support.com."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def lookalike_domain(email: dict) -> int:
    """Lookalike Domain. Przyklad: "Verify information at secure-amazon-support.com."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def unusual_tld(email: dict) -> int:
    """Unusual TLD. Przyklad: "Visit account-verification.xyz.(TLD (Top-Level Domain) is the domain extension, which is the last part of a website address after the final dot.)"

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def long_url(email: dict) -> int:
    """Long URL. Przyklad: "A very long URL is used to hide the true destination."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def ip_address_url(email: dict) -> int:
    """IP Address URL. Przyklad: "Access your account at http://192.168.1.xx/login.(xx change to some IP in project)"

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def encoded_url(email: dict) -> int:
    """Encoded URL. Przyklad: "The URL contains encoded characters."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def hidden_url_destination(email: dict) -> int:
    """Hidden URL Destination. Przyklad: "The displayed link and destination differ."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def shortened_url(email: dict) -> int:
    """Shortened URL. Przyklad: "Open bit.ly/accountverify."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def url_redirect_chain(email: dict) -> int:
    """URL Redirect Chain. Przyklad: "The link redirects through several websites."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def multiple_subdomains(email: dict) -> int:
    """Multiple Subdomains. Przyklad: "login.verify.account.security.company.com"

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def excessive_hyphens(email: dict) -> int:
    """Excessive Hyphens. Przyklad: "secure-account-verification-login.com"

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def suspicious_attachment(email: dict) -> int:
    """Suspicious Attachment. Przyklad: "Please open the attached document."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def zip_attachment(email: dict) -> int:
    """ZIP Attachment. Przyklad: "Important information is in the ZIP archive."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def rar_attachment(email: dict) -> int:
    """RAR Attachment. Przyklad: "Review the attached compressed file."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def exe_attachment(email: dict) -> int:
    """EXE Attachment. Przyklad: "Run the attached application."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def macro_enabled_document(email: dict) -> int:
    """Macro Enabled Document. Przyklad: "Enable macros to view this document."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def password_protected_archive(email: dict) -> int:
    """Password Protected Archive. Przyklad: "Use the provided password to open the file."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def unexpected_invoice(email: dict) -> int:
    """Unexpected Invoice. Przyklad: "Please review the attached invoice."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def unexpected_receipt(email: dict) -> int:
    """Unexpected Receipt. Przyklad: "Your payment receipt is attached."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def unexpected_contract(email: dict) -> int:
    """Unexpected Contract. Przyklad: "Review the attached agreement."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def unexpected_document(email: dict) -> int:
    """Unexpected Document. Przyklad: "Please open the attached file."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def enable_content_request(email: dict) -> int:
    """Enable Content Request. Przyklad: "Enable content to continue."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def disable_protection_request(email: dict) -> int:
    """Disable Protection Request. Przyklad: "Disable Protected View to read the document."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def software_installation_request(email: dict) -> int:
    """Software Installation Request. Przyklad: "Install the attached security update."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def qr_code_login(email: dict) -> int:
    """QR Code Login. Przyklad: "Scan the QR code to sign in."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def qr_code_payment(email: dict) -> int:
    """QR Code Payment. Przyklad: "Scan the code to complete payment."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def generic_greeting(email: dict) -> int:
    """Generic Greeting. Przyklad: "Dear Customer."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def non_personalized_greeting(email: dict) -> int:
    """Non Personalized Greeting. Przyklad: "Dear User."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def missing_recipient_name(email: dict) -> int:
    """Missing Recipient Name. Przyklad: "Hello user."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def grammar_errors(email: dict) -> int:
    """Grammar Errors. Przyklad: "Your account requiring immediate verify."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def spelling_errors(email: dict) -> int:
    """Spelling Errors. Przyklad: "Please complet account verificashion."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def machine_translation_style(email: dict) -> int:
    """Machine Translation Style. Przyklad: "Your account need checking immediately."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def mixed_languages(email: dict) -> int:
    """Mixed Languages. Przyklad: "Please verify your konto now."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def excessive_capitalization(email: dict) -> int:
    """Excessive Capitalization. Przyklad: "VERIFY YOUR ACCOUNT NOW."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def excessive_exclamation_marks(email: dict) -> int:
    """Excessive Exclamation Marks. Przyklad: "Your account will be closed!!!"

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def emotional_manipulation(email: dict) -> int:
    """Emotional Manipulation. Przyklad: "Your help can save a life."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fear_appeal(email: dict) -> int:
    """Fear Appeal. Przyklad: "Your account is at risk."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


FEATURES = {
    "urgency": urgency,
    "time_pressure": time_pressure,
    "threat_of_account_suspension": threat_of_account_suspension,
    "threat_of_data_loss": threat_of_data_loss,
    "threat_of_service_interruption": threat_of_service_interruption,
    "security_alert_with_checking_pressure": security_alert_with_checking_pressure,
    "immediately_account_recovery_request": immediately_account_recovery_request,
    "password_reset_request": password_reset_request,
    "credential_request": credential_request,
    "login_verification_request": login_verification_request,
    "repeated_login_prompt": repeated_login_prompt,
    "microsoft_login_redirect": microsoft_login_redirect,
    "google_login_redirect": google_login_redirect,
    "bank_login_redirect": bank_login_redirect,
    "fake_login_page": fake_login_page,
    "personal_data_request": personal_data_request,
    "pesel_request": pesel_request,
    "national_id_request": national_id_request,
    "passport_request": passport_request,
    "birth_date_request": birth_date_request,
    "address_request": address_request,
    "phone_number_request": phone_number_request,
    "credit_card_request": credit_card_request,
    "cvv_request": cvv_request,
    "pin_request": pin_request,
    "bank_account_request": bank_account_request,
    "security_question_request": security_question_request,
    "document_upload_request": document_upload_request,
    "misspelled_brand_name": misspelled_brand_name,
    "misspelled_domain": misspelled_domain,
    "typosquatting_domain": typosquatting_domain,
    "lookalike_domain": lookalike_domain,
    "unusual_tld": unusual_tld,
    "long_url": long_url,
    "ip_address_url": ip_address_url,
    "encoded_url": encoded_url,
    "hidden_url_destination": hidden_url_destination,
    "shortened_url": shortened_url,
    "url_redirect_chain": url_redirect_chain,
    "multiple_subdomains": multiple_subdomains,
    "excessive_hyphens": excessive_hyphens,
    "suspicious_attachment": suspicious_attachment,
    "zip_attachment": zip_attachment,
    "rar_attachment": rar_attachment,
    "exe_attachment": exe_attachment,
    "macro_enabled_document": macro_enabled_document,
    "password_protected_archive": password_protected_archive,
    "unexpected_invoice": unexpected_invoice,
    "unexpected_receipt": unexpected_receipt,
    "unexpected_contract": unexpected_contract,
    "unexpected_document": unexpected_document,
    "enable_content_request": enable_content_request,
    "disable_protection_request": disable_protection_request,
    "software_installation_request": software_installation_request,
    "qr_code_login": qr_code_login,
    "qr_code_payment": qr_code_payment,
    "generic_greeting": generic_greeting,
    "non_personalized_greeting": non_personalized_greeting,
    "missing_recipient_name": missing_recipient_name,
    "grammar_errors": grammar_errors,
    "spelling_errors": spelling_errors,
    "machine_translation_style": machine_translation_style,
    "mixed_languages": mixed_languages,
    "excessive_capitalization": excessive_capitalization,
    "excessive_exclamation_marks": excessive_exclamation_marks,
    "emotional_manipulation": emotional_manipulation,
    "fear_appeal": fear_appeal,
}
