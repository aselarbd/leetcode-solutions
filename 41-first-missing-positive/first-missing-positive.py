class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        pos = {n: True for n in nums if n > 0}
        
        i = 0
        for i in range(1,len(nums)+2):
            if i not in pos:
                return i
        return i

        