import json
import argparse

from parsers.csv_parser import read_csv
from parsers.resume_parser import read_resume

from normalizer import (
    normalize_email,
    normalize_phone,
    normalize_skills
)

from merger import merge_data
from confidence import calculate_confidence
from projection import project
from validator import validate
from Provenance import generate_provenance


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--config",
        default="config/default.json",
        help="Projection configuration file"
    )

    args = parser.parse_args()

    # -------------------------
    # Read Input
    # -------------------------

    csv_data = read_csv("input/recruiter.csv")
    resume_data = read_resume("input/resume.txt")

    # -------------------------
    # Normalize
    # -------------------------

    csv_data["emails"] = normalize_email(
        csv_data.get("emails", [])
    )

    csv_data["phones"] = normalize_phone(
        csv_data.get("phones", [])
    )

    resume_data["emails"] = normalize_email(
        resume_data.get("emails", [])
    )

    resume_data["phones"] = normalize_phone(
        resume_data.get("phones", [])
    )

    resume_data["skills"] = normalize_skills(
        resume_data.get("skills", [])
    )

    # -------------------------
    # Merge
    # -------------------------

    candidate = merge_data(
        csv_data,
        resume_data
    )

    # -------------------------
    # Confidence
    # -------------------------

    candidate = calculate_confidence(candidate)

    # -------------------------
    # Provenance
    # -------------------------

    provenance = generate_provenance(
        csv_data,
        resume_data
    )

    # -------------------------
    # Validate
    # -------------------------

    errors = validate(candidate)

    if errors:

        print("\nValidation Errors")

        for error in errors:
            print("-", error)

        return

    # -------------------------
    # Load Config
    # -------------------------

    with open(args.config, "r") as file:
        config = json.load(file)

    # -------------------------
    # Projection
    # -------------------------

    projected_candidate = project(
        candidate,
        config
    )

    # -------------------------
    # Final Output
    # -------------------------

    output = {
        "candidate": projected_candidate,
        "confidence": candidate["confidence"],
        "overall_confidence": candidate["overall_confidence"],
        "provenance": provenance
    }

    # -------------------------
    # Save JSON
    # -------------------------

    with open("output/profile.json", "w") as file:

        json.dump(
            output,
            file,
            indent=4
        )

    # -------------------------
    # Print
    # -------------------------

    print("\nFinal Candidate Profile")
    print("-" * 50)

    print(
        json.dumps(
            output,
            indent=4
        )
    )

    print("\nProfile saved successfully!")
    print("Output File : output/profile.json")


if __name__ == "__main__":
    main()