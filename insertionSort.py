def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(array, j, j - 1)
            j -= 1
    return array

def swap(array, indexOne, indexTwo):
        temp = array[indexOne]
        array[indexOne] = array[indexTwo]
        array[indexTwo] = temp