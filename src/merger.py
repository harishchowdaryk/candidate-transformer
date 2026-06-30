"""
merger.py

This module merges data from different sources
into one canonical candidate profile.
"""

from utils import remove_duplicates


def merge_data(csv_data, resume_data):
    """
    Merge recruiter CSV data and resume data.
    """

    merged = {}

    # Name
    merged["full_name"] = csv_data.get("full_name", "")

    # Emails
    merged["emails"] = remove_duplicates(
        csv_data.get("emails", [])
        + resume_data.get("emails", [])
    )

    # Phones
    merged["phones"] = remove_duplicates(
        csv_data.get("phones", [])
        + resume_data.get("phones", [])
    )

    # Location
    merged["location"] = csv_data.get("location", "")

    # Skills
    merged["skills"] = remove_duplicates(
        resume_data.get("skills", [])
    )

    # Education
    merged["education"] = resume_data.get("education", "")

    # Experience
    merged["experience"] = resume_data.get("experience", "")

    return merged