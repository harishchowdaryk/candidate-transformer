"""
resume_parser.py

This module reads candidate information from a resume text file.
"""

import re


def read_resume(file_path):
    """
    Reads the resume text file and extracts
    candidate information.
    """

    try:

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

        candidate = {}

        # -------------------------------
        # Extract Email
        # -------------------------------
        email_match = re.search(
            r'[\w\.-]+@[\w\.-]+\.\w+',
            text
        )

        if email_match:
            candidate["emails"] = [email_match.group()]
        else:
            candidate["emails"] = []

        # -------------------------------
        # Extract Phone
        # -------------------------------
        phone_match = re.search(
            r'(\+91\s?)?\d{10}',
            text
        )

        if phone_match:
            candidate["phones"] = [phone_match.group()]
        else:
            candidate["phones"] = []

        # -------------------------------
        # Extract Skills
        # -------------------------------
        available_skills = [
            "Java",
            "Python",
            "Spring Boot",
            "Docker",
            "SQL",
            "HTML",
            "CSS",
            "JavaScript",
            "React",
            "Node.js",
            "MongoDB",
            "MySQL"
        ]

        skills_found = []

        for skill in available_skills:

            if skill.lower() in text.lower():
                skills_found.append(skill)

        candidate["skills"] = skills_found

        # -------------------------------
        # Extract Education
        # -------------------------------
        education = ""

        education_patterns = [
            "B.E",
            "B.Tech",
            "M.Tech",
            "BCA",
            "MCA",
            "Computer Science"
        ]

        for item in education_patterns:

            if item.lower() in text.lower():
                education = item
                break

        candidate["education"] = education

        # -------------------------------
        # Experience
        # -------------------------------
        if "fresher" in text.lower():
            candidate["experience"] = "Fresher"
        else:
            candidate["experience"] = ""

        return candidate

    except FileNotFoundError:
        print(f"Error: Resume file '{file_path}' not found.")
        return {}

    except Exception as e:
        print(f"Resume Parser Error: {e}")
        return {}