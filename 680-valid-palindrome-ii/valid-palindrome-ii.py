class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1

        while l<r:
            if s[l] != s[r]:
                p1 = s[:l] + s[l+1:]
                p2 = s[:r] + s[r+1:]
                if p1 == p1[::-1] or p2 == p2[::-1]:
                    return True
                else:
                    return False
            l+=1
            r-=1

        return True

        


        