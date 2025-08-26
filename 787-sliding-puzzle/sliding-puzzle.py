import copy
from collections import deque

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        win = [[1, 2, 3], [4, 5, 0]]

        def get_neighbours(pos):
            res, delta_x, delta_y = [], [-1,0,1,0], [0,1,0,-1]

            x = 0 if 0 in pos[0] else 1
            y = pos[x].index(0)
            
            for i in range(4):
                pos_copy =  copy.deepcopy(pos)
                new_x, new_y = x+delta_x[i], y+delta_y[i]
                if 0<= new_x < 2 and 0<=new_y <3:
                    pos_copy[new_x][new_y], pos_copy[x][y] = pos_copy[x][y], pos_copy[new_x][new_y]
                    
                    res.append(pos_copy)
            return res

        queue, visited,i = deque([(board,0)]), set(str(board)), 0

        while queue:
            node,i = queue.popleft()
            
            if node == win:
                return i
                
            for pos in get_neighbours(node):
                if str(pos) not in visited:
                    queue.append((pos,i+1))
                    visited.add(str(pos))
        return -1