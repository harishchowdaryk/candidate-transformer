def remove_duplicates(items):
    """
    Remove duplicate items while keeping the original order.
    """

    unique_items = []

    for item in items:

        if item not in unique_items:
            unique_items.append(item)

    return unique_items