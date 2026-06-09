class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        l = 0
        r = 1
        maxProfit = 0
        while r < len(prices):
            tempProfit = prices[r] - prices[l]
            if tempProfit > maxProfit:
                maxProfit = tempProfit
            if prices[r] < prices[l]:
                l = r
            r += 1
        return maxProfit

        