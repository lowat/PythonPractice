def threeNumberSum(array, targetSum):
    return findTriplets(sorted(array), targetSum)

def findTriplets(array, targetSum):
    triplets = []
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[left] + array[i] + array[right]
            if currentSum == targetSum:
                triplets.append([array[i], array[left], array[right]])
                left += 1
                right -= 1
            elif currentSum > targetSum:
                right -= 1
            else:
                left += 1
    return triplets