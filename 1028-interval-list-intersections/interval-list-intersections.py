class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:

        res,i,j = [],0,0

        while i < len(firstList) and j < len(secondList):
            f = firstList[i]
            s = secondList[j]

            if not ( f[1] < s[0] or  s[1] < f[0] ):
                res.append([max(f[0],s[0]), min(f[1],s[1])])
                
            if f[1] > s[1]:
                j +=1
            else:
                i +=1
        
        return res


        