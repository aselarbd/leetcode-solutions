class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def can_eat_banana(m):
            tot = 0
            for p in piles:
                tot += (p + m - 1) // m
            return tot <= h 
        
        l,r,res  = 1,max(piles),-1

        while l <= r:
            m = (l+r)//2

            if can_eat_banana(m):
                res = m
                r = m-1
            else:
                l = m+1
        return res

        