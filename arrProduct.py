class Solution:
    def productExceptSelf(self, nums):
        result = [1 for num in nums]

        for i in range(1, len(nums)):
            result[i] = nums[i - 1] * result[i - 1]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result