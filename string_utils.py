def split_before_each_uppercases(formula):
    """
    Split a string before each uppercase letter.
    Keep uppercase letters in the output chunks.

    Example:
    "C6H12O6" → ["C6", "H12", "O6"]
    """
    if not formula:
        return []

    parts = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i

    parts.append(formula[start:])
    return parts


def split_at_first_digit(formula):
    """
    Split the string into:
    - prefix (before the first digit)
    - number (first digit onward) as int

    If no digit exists, return (formula, 1).
    """
    for i, ch in enumerate(formula):
        if ch.isdigit():
            prefix = formula[:i]
            number = int(formula[i:])
            return prefix, number

    # No digits found
    return formula, 1

