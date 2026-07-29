class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lower = prices[0]

        for price in prices:
            profit = price - lower 
            res = max(res, profit)
            lower = min(lower, price)
        return res 