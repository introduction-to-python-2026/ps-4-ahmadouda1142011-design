def split_before_each_uppercases(formula):

    if formula == "":
        return []

    parts = []
    start = 0

    for i in range(1, len(formula)):
        if formula[i].isupper():
            part = formula[start:i]
            parts.append(part)
            start = i

    last_part = formula[start:]
    parts.append(last_part)

    return parts








def split_at_first_digit(formula):

    for i in range(len(formula)):
        if formula[i].isdigit():
            j = i
            while j < len(formula) and formula[j].isdigit():
                j += 1
            prefix = formula[:i]
            number_text = formula[i:j]
            number = int(number_text)
            return prefix, number
    return formula, 1
