from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans,l,window = 0,0, deque([])

        for r in range(len(s)):
            window.append(s[r])

            while len(window) != len(set(window)):
                window.popleft()
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans

        