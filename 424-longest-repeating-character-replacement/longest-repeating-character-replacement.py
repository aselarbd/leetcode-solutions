from collections import deque

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, window, ans, freq = 0, deque([]), 0 , {}

        for r in range(len(s)):
            c = s[r]
            window.append(c)
            freq[c] = freq.get(c,0) + 1


            while (r-l+1 - max(freq.values())) > k:
                window.popleft()
                freq[s[l]] -= 1
                l += 1
            
            ans = max(ans, r-l+1)
        
        return ans
                
