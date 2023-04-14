def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    return calcTandemSpeed(redShirtSpeeds, blueShirtSpeeds, fastest)

def calcTandemSpeed(tandemPoolA, tandemPoolB, fastest):
    indexA = 0
    indexB = len(tandemPoolB) - 1 if fastest else 0
    deltaA = 1
    deltaB = -1 if fastest else 1
    tandemSpeed = 0
    while(indicesAreValid(indexA, indexB, len(tandemPoolA), len(tandemPoolB))):
        tandemSpeed += max(tandemPoolA[indexA], tandemPoolB[indexB])
        indexA += deltaA
        indexB += deltaB
    return tandemSpeed


def indicesAreValid(indexA, indexB, listA_length, listB_length):
    return indexA >= 0 and indexA < listA_length and indexB >= 0 and indexB < listB_length