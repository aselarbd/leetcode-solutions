class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice,profit = prices[0],0

        for sellPrice in prices:
            minPrice = min(minPrice, sellPrice)
            profit = max(profit, sellPrice - minPrice)

        return profit

        