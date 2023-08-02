def sweetAndSavory(dishes, target):
    dishes.sort()
    left, right = 0, len(dishes) - 1
    bestPair = [0, 0]
    closestValue = float('inf')
    while(left < right and dishes[left] < 0 and dishes[right] > 0):
        currentPairValue = dishes[left] + dishes[right]
        if currentPairValue > target:
            right -= 1
            continue
        currentDiff = target - currentPairValue
        if currentDiff <= closestValue:
            bestPair[0] = dishes[left]
            bestPair[1] = dishes[right]
            closestValue = currentDiff
        left += 1
    return bestPair