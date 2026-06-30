"""
confidence.py

This module calculates confidence scores
for candidate data.
"""


def calculate_confidence(candidate):
    """
    Calculate confidence score for each field.
    """

    confidence = {}

    for key, value in candidate.items():

        if isinstance(value, list):

            if len(value) > 0:
                confidence[key] = 1.0
            else:
                confidence[key] = 0.0

        else:

            if value:
                confidence[key] = 1.0
            else:
                confidence[key] = 0.0

    overall = sum(confidence.values()) / len(confidence)

    candidate["confidence"] = confidence
    candidate["overall_confidence"] = round(overall, 2)

    return candidate