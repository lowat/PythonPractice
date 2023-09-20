class Solution(object):
    def maxProfit(self, prices):
        lowest, profit = prices[0], 0
        for price in prices[1:]:
            if price < lowest:
                lowest = price
            else:
                profit = max(profit, price - lowest)
        return profit