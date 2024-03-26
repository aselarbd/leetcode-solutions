class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        k=0
        for n in nums:
            if n>0 and -n in nums:
                k = max(k,n)
        
        return -1 if k==0 else k


        