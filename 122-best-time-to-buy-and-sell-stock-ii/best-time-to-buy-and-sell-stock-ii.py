class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        
        profit = 0

        for i in range(len(prices)):
            
            if i>0 and prices[i-1] < prices[i] :
                profit += prices[i] - prices[i-1]

        return profit


        