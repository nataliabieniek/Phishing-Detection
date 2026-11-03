"""Cechy phishingowe - Natalia.

Zakres: cechy nr 68-135 z docs/ProjektDzikieWilki.xlsx (68 funkcji).

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


def _match(text: str, patterns: list) -> int:
    """1 jesli ktorykolwiek wzorzec regex pasuje do `text`, inaczej 0."""
    return int(any(re.search(p, text) for p in patterns))


def curiosity_trigger(email: dict) -> int:
    """Curiosity Trigger. Przyklad: "You need to see this confidential document."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"confidential",
        r"see this",
        r"you won'?t believe",
        r"secret",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def greed_appeal(email: dict) -> int:
    """Greed Appeal. Przyklad: "Earn money with no effort."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"earn (easy )?money",
        r"no effort",
        r"make money",
        r"get rich",
        r"easy money",
        r"\$\d[\d,]*\s*(a|per) (day|week)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def reward_promise(email: dict) -> int:
    """Reward Promise. Przyklad: "Claim your reward now."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"claim your (reward|gift|bonus)",
        r"reward",
        r"free gift",
        r"bonus",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def lottery_winner_claim(email: dict) -> int:
    """Lottery Winner Claim. Przyklad: "You have won a prize."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"you (have )?won",
        r"lottery",
        r"winner",
        r"jackpot",
        r"sweepstake",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def inheritance_scam(email: dict) -> int:
    """Inheritance Scam. Przyklad: "You are entitled to a large inheritance."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"inheritance",
        r"deceased",
        r"next of kin",
        r"late (father|husband|client)",
        r"beneficiary",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def tax_refund_scam(email: dict) -> int:
    """Tax Refund Scam. Przyklad: "Claim your tax refund."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"tax refund",
        r"refund.{0,20}tax",
        r"irs",
        r"hmrc",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def investment_scam(email: dict) -> int:
    """Investment Scam. Przyklad: "Guaranteed profit with no risk."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"guaranteed (profit|return)",
        r"no risk",
        r"risk[- ]free",
        r"investment opportunity",
        r"high returns?",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def cryptocurrency_scam(email: dict) -> int:
    """Cryptocurrency Scam. Przyklad: "Double your crypto investment today."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"crypto",
        r"bitcoin",
        r"\bbtc\b",
        r"ethereum",
        r"double your",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def charity_donation_request(email: dict) -> int:
    """Charity Donation Request. Przyklad: "Help vulnerable children today."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"donat",
        r"charity",
        r"help (vulnerable|children|the poor)",
        r"fundrais",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_charity_campaign(email: dict) -> int:
    """Fake Charity Campaign. Przyklad: "Donate to support disaster victims."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"donate to (support|help)",
        r"relief fund",
        r"disaster victims",
        r"charity campaign",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def disaster_victim_impersonation(email: dict) -> int:
    """Disaster Victim Impersonation. Przyklad: "My family lost everything in the flood."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"lost everything",
        r"flood",
        r"earthquake",
        r"hurricane",
        r"tsunami",
        r"fire destroyed",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def war_victim_impersonation(email: dict) -> int:
    """War Victim Impersonation. Przyklad: "I am a refugee and need urgent assistance."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"refugee",
        r"\bwar\b",
        r"civil war",
        r"fled (the|my) country",
        r"displaced",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def cancer_patient_impersonation(email: dict) -> int:
    """Cancer Patient Impersonation. Przyklad: "I need financial help for treatment."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"cancer",
        r"chemotherapy",
        r"tumou?r",
        r"financial help for treatment",
        r"terminal(ly)? ill",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def disabled_person_impersonation(email: dict) -> int:
    """Disabled Person Impersonation. Przyklad: "Support my medical recovery."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"disabled",
        r"disability",
        r"wheelchair",
        r"medical recovery",
        r"handicap",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def orphan_impersonation(email: dict) -> int:
    """Orphan Impersonation. Przyklad: "I need support after losing my parents."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"orphan",
        r"losing my parents",
        r"lost my parents",
        r"parents (died|passed)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def elderly_person_impersonation(email: dict) -> int:
    """Elderly Person Impersonation. Przyklad: "I lost my life savings."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"life savings",
        r"elderly",
        r"\bpensioner\b",
        r"i am \d{2} years old",
        r"old widow",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def single_parent_impersonation(email: dict) -> int:
    """Single Parent Impersonation. Przyklad: "Help me provide for my children."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"single (mother|father|parent)",
        r"provide for my children",
        r"my (kids|children) (need|are)",
        r"widow",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def animal_rescue_scam(email: dict) -> int:
    """Animal Rescue Scam. Przyklad: "Donate to save abandoned animals."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"abandoned animals",
        r"animal (rescue|shelter)",
        r"save (the )?(dogs|cats|animals)",
        r"stray",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def authority_abuse(email: dict) -> int:
    """Authority Abuse. Przyklad: "Management requires immediate action."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"management (requires|requests)",
        r"immediate action",
        r"by order of",
        r"director requires",
        r"executive team",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def ceo_fraud(email: dict) -> int:
    """CEO Fraud. Przyklad: "The CEO requests an urgent transfer."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"\bceo\b",
        r"chief executive",
        r"the president requests",
        r"managing director",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_hr_request(email: dict) -> int:
    """Fake HR Request. Przyklad: "HR requires employee verification."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"\bhr\b",
        r"human resources",
        r"employee verification",
        r"payroll department",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_it_request(email: dict) -> int:
    """Fake IT Request. Przyklad: "IT requests a password reset."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"\bit (department|support|helpdesk|team|requests?)",
        r"help ?desk",
        r"system administrator",
        r"password reset",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_legal_department(email: dict) -> int:
    """Fake Legal Department. Przyklad: "A compliance review requires your response."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"legal department",
        r"compliance (review|team|department)",
        r"legal team",
        r"attorney",
        r"law firm",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_government_agency(email: dict) -> int:
    """Fake Government Agency. Przyklad: "Tax authorities require verification."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"tax authorit",
        r"government",
        r"\birs\b",
        r"customs office",
        r"ministry",
        r"police department",
        r"\bfbi\b",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_university_message(email: dict) -> int:
    """Fake University Message. Przyklad: "Student account validation is required."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"student account",
        r"university",
        r"\bcampus\b",
        r"student portal",
        r"registrar",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_bank_alert(email: dict) -> int:
    """Fake Bank Alert. Przyklad: "Suspicious banking activity detected."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"suspicious (banking )?activity",
        r"your bank",
        r"bank account (is|has been)",
        r"unauthori[sz]ed (transaction|transfer)",
        r"banking",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_courier_message(email: dict) -> int:
    """Fake Courier Message. Przyklad: "Your package is awaiting payment."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"\bdhl\b",
        r"\bups\b",
        r"fedex",
        r"\busps\b",
        r"courier",
        r"your package",
        r"parcel",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_paypal_notification(email: dict) -> int:
    """Fake PayPal Notification. Przyklad: "Your PayPal account is limited."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"paypal",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_amazon_notification(email: dict) -> int:
    """Fake Amazon Notification. Przyklad: "Your Amazon account requires verification."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"amazon",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_google_notification(email: dict) -> int:
    """Fake Google Notification. Przyklad: "Your Google account is compromised."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"google",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_microsoft_notification(email: dict) -> int:
    """Fake Microsoft Notification. Przyklad: "Microsoft detected unusual activity."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"microsoft",
        r"office ?365",
        r"outlook",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_apple_notification(email: dict) -> int:
    """Fake Apple Notification. Przyklad: "Apple ID requires revalidation."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"apple id",
        r"\bapple\b",
        r"icloud",
        r"itunes",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_facebook_notification(email: dict) -> int:
    """Fake Facebook Notification. Przyklad: "Unusual login detected on Facebook."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"facebook",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_instagram_notification(email: dict) -> int:
    """Fake Instagram Notification. Przyklad: "Confirm your Instagram account."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"instagram",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_linkedin_notification(email: dict) -> int:
    """Fake LinkedIn Notification. Przyklad: "Update your LinkedIn credentials."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"linkedin",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def confidentiality_request(email: dict) -> int:
    """Confidentiality Request. Przyklad: "Do not discuss this request with anyone."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"do not (discuss|share|tell)",
        r"don'?t (discuss|share|tell)",
        r"strictly confidential",
        r"keep (this|it) (private|secret|confidential)",
        r"confidentiality",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def isolation_attempt(email: dict) -> int:
    """Isolation Attempt. Przyklad: "Only you can handle this task."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"only you",
        r"don'?t tell anyone",
        r"do not tell anyone",
        r"keep (this )?between us",
        r"without (informing|telling)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def secret_payment_request(email: dict) -> int:
    """Secret Payment Request. Przyklad: "Keep this transaction confidential."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"keep this (transaction|payment) (confidential|secret)",
        r"confidential (transaction|payment|transfer)",
        r"discreet(ly)?",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def gift_card_request(email: dict) -> int:
    """Gift Card Request. Przyklad: "Purchase gift cards for urgent business needs."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"gift ?cards?",
        r"itunes card",
        r"google play card",
        r"steam card",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def urgent_payment_request(email: dict) -> int:
    """Urgent Payment Request. Przyklad: "Transfer the funds immediately."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"(transfer|wire|send|pay).{0,30}(immediately|urgent|asap|today)",
        r"urgent (payment|transfer)",
        r"wire transfer",
        r"overdue",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def supplier_change_scam(email: dict) -> int:
    """Supplier Change Scam. Przyklad: "Use our new bank account for payment."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"new bank account",
        r"changed (our )?bank",
        r"updated bank (details|account)",
        r"new account (number|details)",
        r"supplier",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def invoice_redirection_fraud(email: dict) -> int:
    """Invoice Redirection Fraud. Przyklad: "Future payments should be sent here."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"future payments",
        r"redirect.{0,20}payment",
        r"invoice.{0,30}(new|updated) (account|bank)",
        r"payments should be sent",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def vendor_impersonation(email: dict) -> int:
    """Vendor Impersonation. Przyklad: "We have changed our payment details."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"changed our payment",
        r"payment details",
        r"vendor",
        r"remittance",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def business_email_compromise(email: dict) -> int:
    """Business Email Compromise. Przyklad: "Please process this transfer discreetly."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"process this transfer",
        r"wire (the )?funds",
        r"are you available",
        r"i need you to (handle|process)",
        r"urgent task",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_voicemail_notification(email: dict) -> int:
    """Fake Voicemail Notification. Przyklad: "You have received a new voicemail, click here to listen."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"voicemail",
        r"voice ?mail",
        r"missed call",
        r"voice message",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_shared_document(email: dict) -> int:
    """Fake Shared Document. Przyklad: "A document has been shared with you."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"shared with you",
        r"has shared",
        r"document.{0,20}shared",
        r"view (the )?document",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_onedrive_file(email: dict) -> int:
    """Fake OneDrive File. Przyklad: "Please review the file in OneDrive."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"onedrive",
        r"sharepoint",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_google_drive_file(email: dict) -> int:
    """Fake Google Drive File. Przyklad: "A document is available in Google Drive."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"google drive",
        r"google docs",
        r"drive\.google",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_dropbox_file(email: dict) -> int:
    """Fake Dropbox File. Przyklad: "You have received a Dropbox file."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"dropbox",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_teams_message(email: dict) -> int:
    """Fake Teams Message. Przyklad: "You received a message in Microsoft Teams."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"microsoft teams",
        r"\bteams message",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_slack_notification(email: dict) -> int:
    """Fake Slack Notification. Przyklad: "You have been mentioned in Slack."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"slack",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_zoom_meeting(email: dict) -> int:
    """Fake Zoom Meeting. Przyklad: "Review the attached Zoom invitation."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"zoom",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_meeting_invitation(email: dict) -> int:
    """Fake Meeting Invitation. Przyklad: "Accept the meeting invitation."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"meeting invit",
        r"accept the (meeting|invitation)",
        r"you are invited",
        r"join (the )?meeting",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def calendar_update_request(email: dict) -> int:
    """Calendar Update Request. Przyklad: "Review changes to a scheduled event."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"calendar",
        r"scheduled event",
        r"reschedul",
        r"event (update|change)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def service_upgrade_scam(email: dict) -> int:
    """Service Upgrade Scam. Przyklad: "Activate premium features now."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"premium",
        r"activate.{0,20}features",
        r"upgrade (your )?(plan|account|service)",
        r"upgrade now",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def subscription_renewal_notice(email: dict) -> int:
    """Subscription Renewal Notice. Przyklad: "Renew your subscription immediately."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"renew",
        r"subscription",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def expired_subscription_alert(email: dict) -> int:
    """Expired Subscription Alert. Przyklad: "Your subscription has expired."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"(subscription|membership|license|account).{0,20}(has )?expired",
        r"expired (subscription|membership)",
        r"has expired",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def cloud_storage_alert(email: dict) -> int:
    """Cloud Storage Alert. Przyklad: "Your cloud storage is full."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"storage (is )?(full|limit|quota)",
        r"cloud storage",
        r"mailbox (is )?(full|quota)",
        r"out of storage",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def security_patch_request(email: dict) -> int:
    """Security Patch Request. Przyklad: "Install a critical security update."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"security (patch|update)",
        r"critical (update|patch)",
        r"install.{0,20}update",
        r"hotfix",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def system_upgrade_request(email: dict) -> int:
    """System Upgrade Request. Przyklad: "Upgrade your operating system now."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"upgrade.{0,30}(operating system|system|windows|software)",
        r"system upgrade",
        r"os update",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def firmware_update_scam(email: dict) -> int:
    """Firmware Update Scam. Przyklad: "Install the attached firmware update."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"firmware",
        r"bios update",
        r"driver update",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def mobile_security_alert(email: dict) -> int:
    """Mobile Security Alert. Przyklad: "Your smartphone security is at risk."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"smartphone",
        r"mobile (security|device|phone)",
        r"your (phone|iphone|android)",
        r"sim card",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def device_registration_request(email: dict) -> int:
    """Device Registration Request. Przyklad: "Register your device immediately."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"register your device",
        r"device registration",
        r"enroll.{0,20}device",
        r"register.{0,20}(phone|computer)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def unknown_device_warning(email: dict) -> int:
    """Unknown Device Warning. Przyklad: "An unknown device accessed your account."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"unknown device",
        r"new device",
        r"unrecogni[sz]ed (device|login)",
        r"unusual (login|sign[- ]in)",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def account_recovery_scam(email: dict) -> int:
    """Account Recovery Scam. Przyklad: "Recover access using the attached form."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"recover(y)? (access|your account)",
        r"account recovery",
        r"restore (your )?account",
        r"regain access",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def verification_form_request(email: dict) -> int:
    """Verification Form Request. Przyklad: "Fill out the verification form."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"verification form",
        r"fill (out|in).{0,20}form",
        r"complete (the|this) form",
        r"attached form",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def customer_survey_scam(email: dict) -> int:
    """Customer Survey Scam. Przyklad: "Complete a survey and claim a reward."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"survey",
        r"questionnaire",
        r"feedback.{0,20}(reward|gift)",
        r"customer satisfaction",
    ])
    return int(value)  # format zwrotu: 0 lub 1


def fake_cashback_offer(email: dict) -> int:
    """Fake Cashback Offer. Przyklad: "Claim your cashback reward now."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    value = _match(text, [
        r"cash ?back",
        r"money back offer",
    ])
    return int(value)  # format zwrotu: 0 lub 1


FEATURES = {
    "curiosity_trigger": curiosity_trigger,
    "greed_appeal": greed_appeal,
    "reward_promise": reward_promise,
    "lottery_winner_claim": lottery_winner_claim,
    "inheritance_scam": inheritance_scam,
    "tax_refund_scam": tax_refund_scam,
    "investment_scam": investment_scam,
    "cryptocurrency_scam": cryptocurrency_scam,
    "charity_donation_request": charity_donation_request,
    "fake_charity_campaign": fake_charity_campaign,
    "disaster_victim_impersonation": disaster_victim_impersonation,
    "war_victim_impersonation": war_victim_impersonation,
    "cancer_patient_impersonation": cancer_patient_impersonation,
    "disabled_person_impersonation": disabled_person_impersonation,
    "orphan_impersonation": orphan_impersonation,
    "elderly_person_impersonation": elderly_person_impersonation,
    "single_parent_impersonation": single_parent_impersonation,
    "animal_rescue_scam": animal_rescue_scam,
    "authority_abuse": authority_abuse,
    "ceo_fraud": ceo_fraud,
    "fake_hr_request": fake_hr_request,
    "fake_it_request": fake_it_request,
    "fake_legal_department": fake_legal_department,
    "fake_government_agency": fake_government_agency,
    "fake_university_message": fake_university_message,
    "fake_bank_alert": fake_bank_alert,
    "fake_courier_message": fake_courier_message,
    "fake_paypal_notification": fake_paypal_notification,
    "fake_amazon_notification": fake_amazon_notification,
    "fake_google_notification": fake_google_notification,
    "fake_microsoft_notification": fake_microsoft_notification,
    "fake_apple_notification": fake_apple_notification,
    "fake_facebook_notification": fake_facebook_notification,
    "fake_instagram_notification": fake_instagram_notification,
    "fake_linkedin_notification": fake_linkedin_notification,
    "confidentiality_request": confidentiality_request,
    "isolation_attempt": isolation_attempt,
    "secret_payment_request": secret_payment_request,
    "gift_card_request": gift_card_request,
    "urgent_payment_request": urgent_payment_request,
    "supplier_change_scam": supplier_change_scam,
    "invoice_redirection_fraud": invoice_redirection_fraud,
    "vendor_impersonation": vendor_impersonation,
    "business_email_compromise": business_email_compromise,
    "fake_voicemail_notification": fake_voicemail_notification,
    "fake_shared_document": fake_shared_document,
    "fake_onedrive_file": fake_onedrive_file,
    "fake_google_drive_file": fake_google_drive_file,
    "fake_dropbox_file": fake_dropbox_file,
    "fake_teams_message": fake_teams_message,
    "fake_slack_notification": fake_slack_notification,
    "fake_zoom_meeting": fake_zoom_meeting,
    "fake_meeting_invitation": fake_meeting_invitation,
    "calendar_update_request": calendar_update_request,
    "service_upgrade_scam": service_upgrade_scam,
    "subscription_renewal_notice": subscription_renewal_notice,
    "expired_subscription_alert": expired_subscription_alert,
    "cloud_storage_alert": cloud_storage_alert,
    "security_patch_request": security_patch_request,
    "system_upgrade_request": system_upgrade_request,
    "firmware_update_scam": firmware_update_scam,
    "mobile_security_alert": mobile_security_alert,
    "device_registration_request": device_registration_request,
    "unknown_device_warning": unknown_device_warning,
    "account_recovery_scam": account_recovery_scam,
    "verification_form_request": verification_form_request,
    "customer_survey_scam": customer_survey_scam,
    "fake_cashback_offer": fake_cashback_offer,
}
