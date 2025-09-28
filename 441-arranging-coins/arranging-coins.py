class Solution:
    def arrangeCoins(self, n: int) -> int:

        if n ==1:return 1

        res, l, r = -1, 1, n

        while l <= r:
            m = (l+r)//2

            feasiblity = (m/2) * (1+m)

            if feasiblity > n :
                r = m-1
                res = m
            else:
                l = m+1

        return res-1


        