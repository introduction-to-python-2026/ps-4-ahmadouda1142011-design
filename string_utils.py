def split_before_each_uppercases(formula):
 parts = []
    start = 0
    for i in range(1, len(formula)):
        if formula[i].isupper():
            parts.append(formula[start:i])
            start = i
    parts.append(formula[start:])
    return parts









def split_at_first_digit(formula):
   for i, ch in enumerate(formula):
        if ch.isdigit():
            return formula[:i], int(formula[i:])
    return formula, 1

