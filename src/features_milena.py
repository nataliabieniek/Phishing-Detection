"""Cechy phishingowe - Milena.

Zakres: cechy nr 136-200 z docs/ProjektDzikieWilki.xlsx (65 funkcji).

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


def refund_eligibility_notice(email: dict) -> int:
    """Refund Eligibility Notice. Przyklad: "You qualify for a refund."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def overpayment_refund_scam(email: dict) -> int:
    """Overpayment Refund Scam. Przyklad: "We accidentally charged you twice."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def prize_distribution_notice(email: dict) -> int:
    """Prize Distribution Notice. Przyklad: "Arrange delivery of your prize."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def free_vacation_offer(email: dict) -> int:
    """Free Vacation Offer. Przyklad: "Claim your free holiday package."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def travel_voucher_scam(email: dict) -> int:
    """Travel Voucher Scam. Przyklad: "Redeem your travel voucher."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def airline_compensation_scam(email: dict) -> int:
    """Airline Compensation Scam. Przyklad: "You are entitled to compensation."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_hotel_refund(email: dict) -> int:
    """Fake Hotel Refund. Przyklad: "We owe you a hotel booking refund."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def shipping_fee_request(email: dict) -> int:
    """Shipping Fee Request. Przyklad: "Pay a small shipping fee."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def customs_fee_scam(email: dict) -> int:
    """Customs Fee Scam. Przyklad: "Your package requires customs payment."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def warehouse_holding_scam(email: dict) -> int:
    """Warehouse Holding Scam. Przyklad: "Your package is being held."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def package_redelivery_request(email: dict) -> int:
    """Package Redelivery Request. Przyklad: "Confirm delivery details."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def address_confirmation_request(email: dict) -> int:
    """Address Confirmation Request. Przyklad: "Verify your shipping address."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_delivery_failure(email: dict) -> int:
    """Fake Delivery Failure. Przyklad: "Delivery failed due to unpaid fees.t."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def scholarship_scam(email: dict) -> int:
    """Scholarship Scam. Przyklad: "Claim your approved scholarship."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def research_participation_reward(email: dict) -> int:
    """Research Participation Reward. Przyklad: "Receive money for participation."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_payroll_update(email: dict) -> int:
    """Fake Payroll Update. Przyklad: "Update payroll information immediately."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def salary_adjustment_notice(email: dict) -> int:
    """Salary Adjustment Notice. Przyklad: "Confirm your salary details."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def direct_deposit_update(email: dict) -> int:
    """Direct Deposit Update. Przyklad: "Update your banking information."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def expense_reimbursement_scam(email: dict) -> int:
    """Expense Reimbursement Scam. Przyklad: "Claim your reimbursement."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def tax_document_request(email: dict) -> int:
    """Tax Document Request. Przyklad: "Upload tax-related documents."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def insurance_claim_scam(email: dict) -> int:
    """Insurance Claim Scam. Przyklad: "Your claim has been approved."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def insurance_refund_scam(email: dict) -> int:
    """Insurance Refund Scam. Przyklad: "Collect your insurance refund."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def medical_benefit_scam(email: dict) -> int:
    """Medical Benefit Scam. Przyklad: "Claim your healthcare benefit."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_pension_notice(email: dict) -> int:
    """Fake Pension Notice. Przyklad: "Confirm retirement payment details."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def fake_social_security_notice(email: dict) -> int:
    """Fake Social Security Notice. Przyklad: "Verify social security information."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def legal_action_threat(email: dict) -> int:
    """Legal Action Threat. Przyklad: "Legal proceedings will begin soon."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def court_notice_scam(email: dict) -> int:
    """Court Notice Scam. Przyklad: "Review the attached legal notice."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def copyright_violation_claim(email: dict) -> int:
    """Copyright Violation Claim. Przyklad: "Your account violated copyright laws."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def compliance_audit_request(email: dict) -> int:
    """Compliance Audit Request. Przyklad: "Provide required documentation."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def policy_violation_warning(email: dict) -> int:
    """Policy Violation Warning. Przyklad: "Your account violated company policy."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def identity_theft_warning(email: dict) -> int:
    """Identity Theft Warning. Przyklad: "Your identity may have been stolen."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def data_breach_alert(email: dict) -> int:
    """Data Breach Alert. Przyklad: "Your information was exposed."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def privacy_violation_notice(email: dict) -> int:
    """Privacy Violation Notice. Przyklad: "Immediate action is needed."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def regulatory_compliance_request(email: dict) -> int:
    """Regulatory Compliance Request. Przyklad: "Submit verification documents."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def financial_audit_notification(email: dict) -> int:
    """Financial Audit Notification. Przyklad: "Your account requires audit review."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def vendor_verification_request(email: dict) -> int:
    """Vendor Verification Request. Przyklad: "Confirm supplier information."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def procurement_request(email: dict) -> int:
    """Procurement Request. Przyklad: "Review the attached purchase order."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def vip_membership_offer(email: dict) -> int:
    """VIP Membership Offer. Przyklad: "Activate exclusive membership access."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def electricity_account_verification(email: dict) -> int:
    """Electricity Account Verification. Przyklad: "Confirm account ownership."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def gas_service_payment_reminder(email: dict) -> int:
    """Gas Service Payment Reminder. Przyklad: "Pay overdue balance."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def internet_provider_notice(email: dict) -> int:
    """Internet Provider Notice. Przyklad: "Verify account to restore service."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def mobile_carrier_alert(email: dict) -> int:
    """Mobile Carrier Alert. Przyklad: "Confirm mobile account information."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def streaming_service_suspension(email: dict) -> int:
    """Streaming Service Suspension. Przyklad: "Update payment details."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def gaming_account_warning(email: dict) -> int:
    """Gaming Account Warning. Przyklad: "Your account is under review."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def reward_points_expiration(email: dict) -> int:
    """Reward Points Expiration. Przyklad: "Redeem points before expiry."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def disaster_survivor_impersonation(email: dict) -> int:
    """Disaster Survivor Impersonation. Przyklad: "I lost everything during the earthquake and urgently need support."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def login_required_before_donation(email: dict) -> int:
    """Login Required Before Donation. Przyklad: "Log in before making a donation."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def login_required_to_view_message(email: dict) -> int:
    """Login Required To View Message. Przyklad: "Please sign in to read the full message."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def login_required_to_open_attachment(email: dict) -> int:
    """Login Required To Open Attachment. Przyklad: "Sign in before downloading the file."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def login_required_to_view_invoice(email: dict) -> int:
    """Login Required To View Invoice. Przyklad: "Log in to access your invoice."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def login_required_to_access_shared_file(email: dict) -> int:
    """Login Required To Access Shared File. Przyklad: "Authenticate to view the document."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def login_required_to_view_package_information(email: dict) -> int:
    """Login Required To View Package Information. Przyklad: "Sign in to track your package."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def login_required_to_receive_refund(email: dict) -> int:
    """Login Required To Receive Refund. Przyklad: "Authenticate to receive your refund."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def login_required_to_confirm_identity(email: dict) -> int:
    """Login Required To Confirm Identity. Przyklad: "Log in to verify your account."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def login_required_to_update_information(email: dict) -> int:
    """Login Required To Update Information. Przyklad: "Sign in to update details."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def microsoft_credential_harvesting(email: dict) -> int:
    """Microsoft Credential Harvesting. Przyklad: "Log in with your Microsoft account."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def google_credential_harvesting(email: dict) -> int:
    """Google Credential Harvesting. Przyklad: "Sign in with Google to continue."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def facebook_credential_harvesting(email: dict) -> int:
    """Facebook Credential Harvesting. Przyklad: "Authenticate using Facebook credentials."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def instagram_credential_harvesting(email: dict) -> int:
    """Instagram Credential Harvesting. Przyklad: "Log in using Instagram."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def linkedin_credential_harvesting(email: dict) -> int:
    """LinkedIn Credential Harvesting. Przyklad: "Sign in to verify your profile."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def bank_credential_harvesting(email: dict) -> int:
    """Bank Credential Harvesting. Przyklad: "Log in with your online banking credentials."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def university_credential_harvesting(email: dict) -> int:
    """University Credential Harvesting. Przyklad: "Sign in with your student account."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def corporate_credential_harvesting(email: dict) -> int:
    """Corporate Credential Harvesting. Przyklad: "Use your company credentials."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def email_credential_harvesting(email: dict) -> int:
    """Email Credential Harvesting. Przyklad: "Enter your mailbox password."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


def sso_credential_harvesting(email: dict) -> int:
    """SSO Credential Harvesting. Przyklad: "Authenticate through Single Sign-On."

    Zwraca 1 jesli cecha wystepuje w mailu, inaczej 0.
    """
    text = _text(email)
    # TODO: wykryj ceche (slowa kluczowe / regex) w `text`
    value = 0
    return int(value)  # format zwrotu: 0 lub 1


FEATURES = {
    "refund_eligibility_notice": refund_eligibility_notice,
    "overpayment_refund_scam": overpayment_refund_scam,
    "prize_distribution_notice": prize_distribution_notice,
    "free_vacation_offer": free_vacation_offer,
    "travel_voucher_scam": travel_voucher_scam,
    "airline_compensation_scam": airline_compensation_scam,
    "fake_hotel_refund": fake_hotel_refund,
    "shipping_fee_request": shipping_fee_request,
    "customs_fee_scam": customs_fee_scam,
    "warehouse_holding_scam": warehouse_holding_scam,
    "package_redelivery_request": package_redelivery_request,
    "address_confirmation_request": address_confirmation_request,
    "fake_delivery_failure": fake_delivery_failure,
    "scholarship_scam": scholarship_scam,
    "research_participation_reward": research_participation_reward,
    "fake_payroll_update": fake_payroll_update,
    "salary_adjustment_notice": salary_adjustment_notice,
    "direct_deposit_update": direct_deposit_update,
    "expense_reimbursement_scam": expense_reimbursement_scam,
    "tax_document_request": tax_document_request,
    "insurance_claim_scam": insurance_claim_scam,
    "insurance_refund_scam": insurance_refund_scam,
    "medical_benefit_scam": medical_benefit_scam,
    "fake_pension_notice": fake_pension_notice,
    "fake_social_security_notice": fake_social_security_notice,
    "legal_action_threat": legal_action_threat,
    "court_notice_scam": court_notice_scam,
    "copyright_violation_claim": copyright_violation_claim,
    "compliance_audit_request": compliance_audit_request,
    "policy_violation_warning": policy_violation_warning,
    "identity_theft_warning": identity_theft_warning,
    "data_breach_alert": data_breach_alert,
    "privacy_violation_notice": privacy_violation_notice,
    "regulatory_compliance_request": regulatory_compliance_request,
    "financial_audit_notification": financial_audit_notification,
    "vendor_verification_request": vendor_verification_request,
    "procurement_request": procurement_request,
    "vip_membership_offer": vip_membership_offer,
    "electricity_account_verification": electricity_account_verification,
    "gas_service_payment_reminder": gas_service_payment_reminder,
    "internet_provider_notice": internet_provider_notice,
    "mobile_carrier_alert": mobile_carrier_alert,
    "streaming_service_suspension": streaming_service_suspension,
    "gaming_account_warning": gaming_account_warning,
    "reward_points_expiration": reward_points_expiration,
    "disaster_survivor_impersonation": disaster_survivor_impersonation,
    "login_required_before_donation": login_required_before_donation,
    "login_required_to_view_message": login_required_to_view_message,
    "login_required_to_open_attachment": login_required_to_open_attachment,
    "login_required_to_view_invoice": login_required_to_view_invoice,
    "login_required_to_access_shared_file": login_required_to_access_shared_file,
    "login_required_to_view_package_information": login_required_to_view_package_information,
    "login_required_to_receive_refund": login_required_to_receive_refund,
    "login_required_to_confirm_identity": login_required_to_confirm_identity,
    "login_required_to_update_information": login_required_to_update_information,
    "microsoft_credential_harvesting": microsoft_credential_harvesting,
    "google_credential_harvesting": google_credential_harvesting,
    "facebook_credential_harvesting": facebook_credential_harvesting,
    "instagram_credential_harvesting": instagram_credential_harvesting,
    "linkedin_credential_harvesting": linkedin_credential_harvesting,
    "bank_credential_harvesting": bank_credential_harvesting,
    "university_credential_harvesting": university_credential_harvesting,
    "corporate_credential_harvesting": corporate_credential_harvesting,
    "email_credential_harvesting": email_credential_harvesting,
    "sso_credential_harvesting": sso_credential_harvesting,
}
