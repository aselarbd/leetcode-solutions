class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_i = 0

        if len(s) ==0:
            return True
        if len(t) ==0:
            return False

        for c in t:
            if c == s[s_i]:
                s_i +=1
            if s_i >= len(s):
                return True
        return False
        