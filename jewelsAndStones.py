class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewelSet = set(jewels)
        jewelCount = 0
        for stone in stones:
            if stone in jewelSet:
                jewelCount += 1
        return jewelCount