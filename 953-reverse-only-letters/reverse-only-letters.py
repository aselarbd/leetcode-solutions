class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        L,R =0,len(s)-1
        s_list = list(s)

        while L<R:
            if (s_list[L].islower() or s_list[L].isupper())  and (s_list[R].islower() or s_list[R].isupper()):
                s_list[L], s_list[R] = s_list[R], s_list[L]
                L+=1
                R-=1
            elif not ( s_list[L].islower() or s_list[L].isupper()):
                L+=1
            elif not ( s_list[R].islower() or s_list[R].isupper()):
                R-=1
            
        return ''.join(s_list)



        