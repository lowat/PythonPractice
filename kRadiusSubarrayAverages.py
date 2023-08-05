class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        windowSize = k * 2 + 1
        if len(nums) < windowSize:
            return [-1 for num in nums]
        runningSum, left, right = 0, 0, 0
        result = []
        
        while right < len(nums):
            runningSum += nums[right]
            if (right - left) < k:
                result.append(-1)
            elif right - left == windowSize - 1:
                result.append(runningSum // windowSize)
                runningSum -= nums[left]
                left += 1
            right += 1

        diff = len(nums) - len(result)
        for i in range(diff):
            result.append(-1)
        return result