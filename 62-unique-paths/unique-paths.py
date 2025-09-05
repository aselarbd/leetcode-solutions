class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        res = [[0]* (n+1) for _ in range(m+1)]
        res[1][1] = 1

        for i in range(1,m+1):
            for j in range(1,n+1):

                if i==1 and j==1: continue

                res[i][j] = res[i-1][j] + res[i][j-1]
        
        return res[-1][-1]

        