class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n, res, ind = len(strs), "", 0

        while ind < len(min(strs)):
            c = 0
            curr = strs[0][:ind+1]
            for s in strs:
                if s[:ind+1] == curr:
                    c+=1
            if c == n:
                res = strs[0][:ind+1]
                ind +=1
            else:
                break
        return res
                