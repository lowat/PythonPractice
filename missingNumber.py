class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numSet = {num for num in nums}
        for i in range(0,len(nums)):
            if not i in numSet:
                return i
        return len(nums)