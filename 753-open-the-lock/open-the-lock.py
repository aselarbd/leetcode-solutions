from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if "0000" in deadends:
            return -1

        def get_neighbours(curr_combo):
            res = []
            for i,c in enumerate(curr_combo):
                inc, dec = int(c)+1, int(c)-1
                
                if inc == 10:inc = 0
                if dec < 0:dec = 9
                    
                inc_combo =  curr_combo[:i] + str(inc) + curr_combo[i+1:]
                dec_combo = curr_combo[:i] + str(dec) + curr_combo[i+1:]

                if inc_combo not in deadends:
                    res.append(inc_combo)
                if dec_combo not in deadends:
                    res.append(dec_combo)
            return res

        queue, visited, i = deque([("0000",0)]), set("0000"), 0

        while len(queue)>0:
            node,i =  queue.popleft()

            if node == target:
                return i

            for n in get_neighbours(node):
                if n not in visited:
                    queue.append((n,i+1))
                    visited.add(n)
                
        
        return -1
        