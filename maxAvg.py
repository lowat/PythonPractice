class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSum = 0
        for x in range(k):
            maxSum += nums[x]
        
        curSum = maxSum
        for i in range(k, len(nums)):
            curSum += nums[i] - nums[i - k]
            maxSum = max(maxSum, curSum)
        return maxSum / k