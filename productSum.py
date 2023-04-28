def productSum(array, depth = 1):
    sum = 0
    for element in array:
        if type(element) is list:
            sum += productSum(element, depth + 1)
        else:
            sum += element
    return depth * sum