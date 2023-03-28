def bubbleSort(array):
    isSorted = False
    endPointer = len(array) - 1
    while(not isSorted):
        isSorted = True
        for i in range(endPointer):
            if(array[i] > array[i + 1]):
                swap(array, i, i+1)
                isSorted = False
        endPointer -= 1
    return array

def swap(array, indexOne, indexTwo):
    temp = array[indexOne]
    array[indexOne] = array[indexTwo]
    array[indexTwo] = temp