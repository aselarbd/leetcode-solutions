class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        res = []

        for f in firstList:
            for s in secondList:
                if not ( f[1] < s[0] or  s[1] < f[0] ):
                    res.append([max(f[0],s[0]), min(f[1],s[1])])
        
        return res


        