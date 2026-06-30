"""
provenance.py

Tracks where each field of candidate data
was obtained from.
"""


def generate_provenance(csv_data, resume_data):
    """
    Generate provenance information for each field.
    """

    provenance = {}

    # -------------------------
    # Full Name
    # -------------------------
    if csv_data.get("full_name"):
        provenance["full_name"] = ["Recruiter CSV"]

    # -------------------------
    # Emails
    # -------------------------
    email_sources = []

    if csv_data.get("emails"):
        email_sources.append("Recruiter CSV")

    if resume_data.get("emails"):
        email_sources.append("Resume")

    provenance["emails"] = email_sources

    # -------------------------
    # Phones
    # -------------------------
    phone_sources = []

    if csv_data.get("phones"):
        phone_sources.append("Recruiter CSV")

    if resume_data.get("phones"):
        phone_sources.append("Resume")

    provenance["phones"] = phone_sources

    # -------------------------
    # Location
    # -------------------------
    if csv_data.get("location"):
        provenance["location"] = ["Recruiter CSV"]

    # -------------------------
    # Skills
    # -------------------------
    if resume_data.get("skills"):
        provenance["skills"] = ["Resume"]

    # -------------------------
    # Education
    # -------------------------
    if resume_data.get("education"):
        provenance["education"] = ["Resume"]

    # -------------------------
    # Experience
    # -------------------------
    if resume_data.get("experience"):
        provenance["experience"] = ["Resume"]

    return provenance