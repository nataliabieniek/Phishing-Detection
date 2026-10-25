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


def curiosity_trigger(email: dict) -> int:
    """Curiosity Trigger. Przyklad: "You need to see this confidential document."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def greed_appeal(email: dict) -> int:
    """Greed Appeal. Przyklad: "Earn money with no effort."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def reward_promise(email: dict) -> int:
    """Reward Promise. Przyklad: "Claim your reward now."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def lottery_winner_claim(email: dict) -> int:
    """Lottery Winner Claim. Przyklad: "You have won a prize."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def inheritance_scam(email: dict) -> int:
    """Inheritance Scam. Przyklad: "You are entitled to a large inheritance."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def tax_refund_scam(email: dict) -> int:
    """Tax Refund Scam. Przyklad: "Claim your tax refund."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def investment_scam(email: dict) -> int:
    """Investment Scam. Przyklad: "Guaranteed profit with no risk."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def cryptocurrency_scam(email: dict) -> int:
    """Cryptocurrency Scam. Przyklad: "Double your crypto investment today."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def charity_donation_request(email: dict) -> int:
    """Charity Donation Request. Przyklad: "Help vulnerable children today."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_charity_campaign(email: dict) -> int:
    """Fake Charity Campaign. Przyklad: "Donate to support disaster victims."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def disaster_victim_impersonation(email: dict) -> int:
    """Disaster Victim Impersonation. Przyklad: "My family lost everything in the flood."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def war_victim_impersonation(email: dict) -> int:
    """War Victim Impersonation. Przyklad: "I am a refugee and need urgent assistance."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def cancer_patient_impersonation(email: dict) -> int:
    """Cancer Patient Impersonation. Przyklad: "I need financial help for treatment."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def disabled_person_impersonation(email: dict) -> int:
    """Disabled Person Impersonation. Przyklad: "Support my medical recovery."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def orphan_impersonation(email: dict) -> int:
    """Orphan Impersonation. Przyklad: "I need support after losing my parents."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def elderly_person_impersonation(email: dict) -> int:
    """Elderly Person Impersonation. Przyklad: "I lost my life savings."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def single_parent_impersonation(email: dict) -> int:
    """Single Parent Impersonation. Przyklad: "Help me provide for my children."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def animal_rescue_scam(email: dict) -> int:
    """Animal Rescue Scam. Przyklad: "Donate to save abandoned animals."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def authority_abuse(email: dict) -> int:
    """Authority Abuse. Przyklad: "Management requires immediate action."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def ceo_fraud(email: dict) -> int:
    """CEO Fraud. Przyklad: "The CEO requests an urgent transfer."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_hr_request(email: dict) -> int:
    """Fake HR Request. Przyklad: "HR requires employee verification."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_it_request(email: dict) -> int:
    """Fake IT Request. Przyklad: "IT requests a password reset."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_legal_department(email: dict) -> int:
    """Fake Legal Department. Przyklad: "A compliance review requires your response."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_government_agency(email: dict) -> int:
    """Fake Government Agency. Przyklad: "Tax authorities require verification."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_university_message(email: dict) -> int:
    """Fake University Message. Przyklad: "Student account validation is required."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_bank_alert(email: dict) -> int:
    """Fake Bank Alert. Przyklad: "Suspicious banking activity detected."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_courier_message(email: dict) -> int:
    """Fake Courier Message. Przyklad: "Your package is awaiting payment."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_paypal_notification(email: dict) -> int:
    """Fake PayPal Notification. Przyklad: "Your PayPal account is limited."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_amazon_notification(email: dict) -> int:
    """Fake Amazon Notification. Przyklad: "Your Amazon account requires verification."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_google_notification(email: dict) -> int:
    """Fake Google Notification. Przyklad: "Your Google account is compromised."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_microsoft_notification(email: dict) -> int:
    """Fake Microsoft Notification. Przyklad: "Microsoft detected unusual activity."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_apple_notification(email: dict) -> int:
    """Fake Apple Notification. Przyklad: "Apple ID requires revalidation."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_facebook_notification(email: dict) -> int:
    """Fake Facebook Notification. Przyklad: "Unusual login detected on Facebook."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_instagram_notification(email: dict) -> int:
    """Fake Instagram Notification. Przyklad: "Confirm your Instagram account."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_linkedin_notification(email: dict) -> int:
    """Fake LinkedIn Notification. Przyklad: "Update your LinkedIn credentials."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def confidentiality_request(email: dict) -> int:
    """Confidentiality Request. Przyklad: "Do not discuss this request with anyone."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def isolation_attempt(email: dict) -> int:
    """Isolation Attempt. Przyklad: "Only you can handle this task."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def secret_payment_request(email: dict) -> int:
    """Secret Payment Request. Przyklad: "Keep this transaction confidential."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def gift_card_request(email: dict) -> int:
    """Gift Card Request. Przyklad: "Purchase gift cards for urgent business needs."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def urgent_payment_request(email: dict) -> int:
    """Urgent Payment Request. Przyklad: "Transfer the funds immediately."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def supplier_change_scam(email: dict) -> int:
    """Supplier Change Scam. Przyklad: "Use our new bank account for payment."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def invoice_redirection_fraud(email: dict) -> int:
    """Invoice Redirection Fraud. Przyklad: "Future payments should be sent here."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def vendor_impersonation(email: dict) -> int:
    """Vendor Impersonation. Przyklad: "We have changed our payment details."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def business_email_compromise(email: dict) -> int:
    """Business Email Compromise. Przyklad: "Please process this transfer discreetly."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_voicemail_notification(email: dict) -> int:
    """Fake Voicemail Notification. Przyklad: "You have received a new voicemail, click here to listen."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_shared_document(email: dict) -> int:
    """Fake Shared Document. Przyklad: "A document has been shared with you."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_onedrive_file(email: dict) -> int:
    """Fake OneDrive File. Przyklad: "Please review the file in OneDrive."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_google_drive_file(email: dict) -> int:
    """Fake Google Drive File. Przyklad: "A document is available in Google Drive."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_dropbox_file(email: dict) -> int:
    """Fake Dropbox File. Przyklad: "You have received a Dropbox file."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_teams_message(email: dict) -> int:
    """Fake Teams Message. Przyklad: "You received a message in Microsoft Teams."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_slack_notification(email: dict) -> int:
    """Fake Slack Notification. Przyklad: "You have been mentioned in Slack."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_zoom_meeting(email: dict) -> int:
    """Fake Zoom Meeting. Przyklad: "Review the attached Zoom invitation."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_meeting_invitation(email: dict) -> int:
    """Fake Meeting Invitation. Przyklad: "Accept the meeting invitation."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def calendar_update_request(email: dict) -> int:
    """Calendar Update Request. Przyklad: "Review changes to a scheduled event."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def service_upgrade_scam(email: dict) -> int:
    """Service Upgrade Scam. Przyklad: "Activate premium features now."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def subscription_renewal_notice(email: dict) -> int:
    """Subscription Renewal Notice. Przyklad: "Renew your subscription immediately."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def expired_subscription_alert(email: dict) -> int:
    """Expired Subscription Alert. Przyklad: "Your subscription has expired."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def cloud_storage_alert(email: dict) -> int:
    """Cloud Storage Alert. Przyklad: "Your cloud storage is full."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def security_patch_request(email: dict) -> int:
    """Security Patch Request. Przyklad: "Install a critical security update."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def system_upgrade_request(email: dict) -> int:
    """System Upgrade Request. Przyklad: "Upgrade your operating system now."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def firmware_update_scam(email: dict) -> int:
    """Firmware Update Scam. Przyklad: "Install the attached firmware update."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def mobile_security_alert(email: dict) -> int:
    """Mobile Security Alert. Przyklad: "Your smartphone security is at risk."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def device_registration_request(email: dict) -> int:
    """Device Registration Request. Przyklad: "Register your device immediately."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def unknown_device_warning(email: dict) -> int:
    """Unknown Device Warning. Przyklad: "An unknown device accessed your account."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def account_recovery_scam(email: dict) -> int:
    """Account Recovery Scam. Przyklad: "Recover access using the attached form."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def verification_form_request(email: dict) -> int:
    """Verification Form Request. Przyklad: "Fill out the verification form."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def customer_survey_scam(email: dict) -> int:
    """Customer Survey Scam. Przyklad: "Complete a survey and claim a reward."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_cashback_offer(email: dict) -> int:
    """Fake Cashback Offer. Przyklad: "Claim your cashback reward now."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
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
