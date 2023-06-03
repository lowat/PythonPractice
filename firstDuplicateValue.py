def firstDuplicateValue(array):
    unique = set()
    for value in array:
        if value in unique:
            return value
        unique.add(value)
    return -1