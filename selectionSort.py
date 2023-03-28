def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array) - 1:
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(array, smallestIdx, currentIdx)
        currentIdx += 1
    return array


def swap(array, indexOne, indexTwo):
    array[indexTwo], array[indexOne] = array[indexOne], array[indexTwo]
