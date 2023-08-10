class Solution:
    def countElements(self, arr: List[int]) -> int:
        result = 0
        numSet = set(arr)
        for num in arr:
            if num + 1 in arr:
                result += 1
        return result
                
        