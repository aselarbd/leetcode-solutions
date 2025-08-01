class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack  = [] # (index,price)
        res  = prices[:]

        for i,p in enumerate(prices):

            while stack and stack[-1][1] >= p:
                priceI, priceV = stack.pop()
                res[priceI] = priceV - p


            stack.append((i,p))

        return res

        