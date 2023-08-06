class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minStartValue = 1
        prefixSum = 0
        for num in nums:
            prefixSum += num
            minStartValue = max(minStartValue, abs(prefixSum) + 1) if prefixSum < 1 else minStartValue
        return minStartValue