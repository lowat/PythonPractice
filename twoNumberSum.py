def twoNumberSum(array, targetSum):
    targetPairs = {}
    for num in array:
        if (targetSum - num) in targetPairs:
            return [targetSum - num, num]
        else:
            targetPairs[num] = True
    return []