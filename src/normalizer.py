"""
normalizer.py

This module normalizes candidate data such as
emails, phone numbers, and skills.
"""

import phonenumbers
from utils import remove_duplicates


def normalize_email(emails):
    """
    Convert emails to lowercase and remove duplicates.
    """

    normalized = []

    for email in emails:

        email = email.strip().lower()

        normalized.append(email)

    return remove_duplicates(normalized)


def normalize_phone(phones):
    """
    Convert phone numbers to international format (E.164).
    """

    normalized = []

    for phone in phones:

        try:

            number = phonenumbers.parse(phone, "IN")

            formatted = phonenumbers.format_number(
                number,
                phonenumbers.PhoneNumberFormat.E164
            )

            normalized.append(formatted)

        except:

            continue

    return remove_duplicates(normalized)


def normalize_skills(skills):
    """
    Remove duplicate skills and standardize formatting.
    """

    normalized = []

    for skill in skills:

        skill = skill.strip().title()

        normalized.append(skill)

    return remove_duplicates(normalized)