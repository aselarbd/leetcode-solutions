class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l,r,raw = 0, len(matrix) -1, -1

        while l <= r:
            m = (l+r)//2

            if matrix[m][-1] >= target:
                raw =  m
                r = m-1
            else:
                l = m+1
        
        a,b,col = 0,len(matrix[raw])-1, -1

        while a <= b:
            c = (a+b)//2
            if matrix[raw][c] >= target:
                col = c
                b = c-1
            else:
                a = c+1
        
        return matrix[raw][col] == target







