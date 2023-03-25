def binarySearch(array, target):
    leftPointer = 0
    rightPointer = len(array) - 1
    while(leftPointer <= rightPointer):
        midPointer = (leftPointer + rightPointer) // 2
        if(array[midPointer] == target):
            return midPointer
        if(target > array[midPointer]):
            leftPointer = midPointer + 1
        else:
            rightPointer = midPointer - 1
    return -1