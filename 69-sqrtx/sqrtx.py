class Solution:
    def mySqrt(self, x: int) -> int:
        if x in {0,1}:
            return x
        
        l,r,res = 0,x,-1

        while l <= r:
            m = (l+r)//2

            if m**2 == x:
                return m
            elif m**2 > x:
                res = m
                r = m-1
            else:
                l = m+1
        return res-1
        