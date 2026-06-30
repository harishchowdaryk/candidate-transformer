"""
csv_parser.py

This module reads candidate information from a recruiter CSV file.
"""

import pandas as pd


def read_csv(file_path):
    """
    Reads the recruiter CSV file and returns candidate data
    as a dictionary.
    """

    try:
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Check if the file contains data
        if df.empty:
            print("Error: CSV file is empty.")
            return {}

        # Read the first candidate
        row = df.iloc[0]

        candidate = {
            "full_name": str(row.get("Name", "")).strip(),
            "emails": [str(row.get("Email", "")).strip()],
            "phones": [str(row.get("Phone", "")).strip()],
            "location": str(row.get("Location", "")).strip()
        }

        return candidate

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}

    except Exception as e:
        print(f"CSV Parser Error: {e}")
        return {}