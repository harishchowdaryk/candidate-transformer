"""
projection.py

This module creates the final output based on
the runtime configuration.
"""


def get_value(data, path):
    """
    Get value from dictionary using a path.

    Examples:
        emails[0]
        phones[0]
        full_name
    """

    if "[" in path:
        field = path.split("[")[0]
        index = int(path.split("[")[1].split("]")[0])

        values = data.get(field, [])

        if len(values) > index:
            return values[index]

        return None

    return data.get(path)


def project(candidate, config):
    """
    Create the final projected output.
    """

    output = {}

    for field in config["fields"]:

        output[field["path"]] = get_value(
            candidate,
            field["from"]
        )

    return output