class Solution:



    def shortestToChar(self, s: str, c: str) -> List[int]:

        res = [float('inf')] * len(s)   

        for ind, ch in enumerate(s):
            if ch == c:
                res[ind]=0
            else:
                
                right_len = float('inf')
                for i,crr in enumerate(s[ind+1:]):
                    if crr==c:
                        right_len = abs(i+1)
                        break
                
                left_len = float('inf')
                for i,crr in enumerate(s[:ind][::-1]):
                    if crr==c:
                        left_len = abs(i+1)
                        break

                res[ind] = min(right_len, left_len)
        
        return res
