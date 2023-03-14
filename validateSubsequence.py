def isValidSubsequence(array, sequence):
    arrPointer = 0
    seqPointer = 0

    while seqPointer < len(sequence):
        if arrPointer >= len(array):
            return False;
        if array[arrPointer] == sequence[seqPointer]:
            seqPointer += 1;
        arrPointer += 1;

    return seqPointer == len(sequence);