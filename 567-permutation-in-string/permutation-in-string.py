class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        fixC,tempC,l = {}, {}, 0

        for c in s1:
            fixC[c] = fixC.get(c,0) + 1

        for c in s2[:len(s1)]:
            tempC[c] = tempC.get(c,0) +1
        
        for r in range(len(s1), len(s2)):
            if fixC == tempC:
                return True
            
            tempC[s2[r]] = tempC.get(s2[r],0) + 1

            tempC[s2[l]] = tempC[s2[l]] - 1 
            if tempC[s2[l]] <= 0:
                del tempC[s2[l]]
            
            l += 1

        return fixC == tempC

        