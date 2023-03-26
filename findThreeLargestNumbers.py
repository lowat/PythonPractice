def findThreeLargestNumbers(array):
    largestValues = [None, None, None]
    for value in array:
        place_value(largestValues, value)
    return largestValues

def place_value(largestValues, value):
    for index in range(len(largestValues) - 1, -1, -1):
        currentValue = largestValues[index]
        if(currentValue == None or value > currentValue):
            value = replace_value_at_index_with_new_value_and_return(largestValues, index, value)

def replace_value_at_index_with_new_value_and_return(largestValues, index, value):
    displacedValue = largestValues[index]
    largestValues[index] = value
    return displacedValue