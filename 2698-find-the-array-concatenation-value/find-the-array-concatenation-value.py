class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        
        concat = 0
        l,r = 0,len(nums)-1

        while l<r:
           concat += int(str(nums[l])+str(nums[r]))
           l+=1
           r-=1
        
        if l==r:
            concat += nums[l]
        
        return concat

        