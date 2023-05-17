def moveElementToEnd(array, toMove):
    left = 0
    right = len(array) - 1
    while left < right:
        leftValue = array[left]
        rightValue = array[right]
        if leftValue == toMove and rightValue != toMove:
            swap(left, right, array)
        left = left + 1 if leftValue != toMove else left
        right = right - 1 if rightValue == toMove else right
    return array

def swap(idxOne, idxTwo, array):
    array[idxOne], array[idxTwo] = array[idxTwo], array[idxOne]