def isMonotonic(array):
    isNonIncreasing = isNonDecreasing = True
    for i in range(1, len(array)):
        isNonIncreasing = False if not array[i - 1] <= array[i] else isNonIncreasing
        isNonDecreasing = False if not array[i - 1] >= array[i] else isNonDecreasing        
    return isNonIncreasing or isNonDecreasing        