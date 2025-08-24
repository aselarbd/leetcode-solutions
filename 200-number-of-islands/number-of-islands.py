from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        max_r, max_c, count = len(grid), len(grid[0]), 0

        def get_neighbours(r,c):
            res, delta_r, delta_c = [], [-1,0,1,0], [0,1,0,-1]

            for i in range(len(delta_r)):
                new_r, new_c = r-delta_r[i], c-delta_c[i]

                if 0<= new_r < max_r and 0<= new_c < max_c:
                    if grid[new_r][new_c] == "1":
                        res.append((new_r,new_c))
            return res

        for x in range(max_r):
            for y in range(max_c):

                if grid[x][y] == "1":
                    count += 1
                
                    queue, visit = deque([(x,y)]), set((x,y))

                    while len(queue) >0:

                        c_x, c_y = queue.pop()
                        grid[c_x][c_y] = "-1"

                        for n in get_neighbours(c_x, c_y):
                            if n not in visit:
                                queue.append(n)
                                visit.add(n)
        
        return count
