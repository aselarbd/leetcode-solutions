class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        col = defaultdict(set)
        raw = defaultdict(set)
        squre = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in col[c] or 
                board[r][c] in raw[r] or 
                board[r][c] in squre[(r//3,c//3)]):
                    return False
            
                raw[r].add(board[r][c])
                col[c].add(board[r][c])
                squre[(r//3,c//3)].add(board[r][c])
        return True
