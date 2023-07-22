def missingNumbers(nums):
    targetLine = findTargetLine(nums)
    targetHalfSums = getTargetHalfSums(len(nums), targetLine)
    actualHalfSums = getActualHalfSums(nums, targetLine)
    firstHalfMissing = targetHalfSums[0] - actualHalfSums[0]
    secondHalfMissing = targetHalfSums[1] - actualHalfSums[1]
    return [firstHalfMissing, secondHalfMissing]

def findTargetLine(nums):
    total = sum(range(1, len(nums)+3))
    for num in nums:
        total -= num
    cutoffLine = total // 2
    return cutoffLine

def getTargetHalfSums(arrLength, targetLine):
    firstTargetHalfSum = sum(range(1, targetLine + 1))
    secondTargetHalfSum = sum(range(targetLine + 1, arrLength + 3))
    return (firstTargetHalfSum, secondTargetHalfSum)

def getActualHalfSums(nums, targetLine):
    firstActualHalfSum = 0
    secondActualHalfSum = 0
    for num in nums:
        if num <= targetLine:
            firstActualHalfSum += num
        else:
            secondActualHalfSum += num
    return (firstActualHalfSum, secondActualHalfSum)