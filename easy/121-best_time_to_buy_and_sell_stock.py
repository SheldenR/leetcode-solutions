class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxProfit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(price - minPrice, maxProfit)

        return maxProfit
