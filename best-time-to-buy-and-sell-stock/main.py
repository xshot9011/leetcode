# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minValue = prices[0] 
        # O(n)
        for i in range(1, len(prices)):
            currentValue = prices[i]
            if currentValue < minValue:
                minValue = prices[i]
            else:
                profit = max(profit, currentValue - minValue)
        return profit
