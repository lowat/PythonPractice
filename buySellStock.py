class Solution(object):
    def maxProfit(self, prices):
        lowest = prices[0]
        profit = 0
        for price in prices[1:]:
            if price < lowest:
                lowest = price
                continue
            else:
                profit = max(profit, price - lowest)
        return profit