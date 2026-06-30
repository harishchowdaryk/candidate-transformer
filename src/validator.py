"""
validator.py

This module validates the final candidate profile.
"""


def validate(candidate):
    """
    Validate required fields.
    """

    required_fields = [
        "full_name",
        "emails",
        "phones"
    ]

    errors = []

    for field in required_fields:

        value = candidate.get(field)

        if value is None:
            errors.append(f"{field} is missing")

        elif isinstance(value, list) and len(value) == 0:
            errors.append(f"{field} is empty")

        elif isinstance(value, str) and value.strip() == "":
            errors.append(f"{field} is empty")

    return errors