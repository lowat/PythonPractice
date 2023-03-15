def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]
    largerValueIdx = len(array) - 1
    smallerValueIdx = 0
    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIdx]
        
        if abs(smallerValue) > abs(largerValue):
            sortedSquares[idx] = smallerValue * smallerValue
            smallerValueIdx += 1
        else:
            sortedSquares[idx] = largerValue * largerValue
            largerValueIdx -= 1
    return sortedSquares
