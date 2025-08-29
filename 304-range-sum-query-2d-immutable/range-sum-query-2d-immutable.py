class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.prefMat = []
        for row in matrix:
            pref = 0
            prefRow = []
            for i in range(len(row)):
                pref += row[i]
                prefRow.append(pref)
            self.prefMat.append(prefRow)

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        tot = 0
        for i in range(row1, row2+1):
            tot += self.prefMat[i][col2] - (self.prefMat[i][col1-1] if col1 > 0 else 0)
        return tot

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)