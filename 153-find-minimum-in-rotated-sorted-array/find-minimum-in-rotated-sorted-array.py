class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r,res = 0,len(nums)-1,-1

        while l <= r:
            m = (l+r)//2

            if nums[m]<= nums[-1]:
                res = m
                r = m-1
            else:
                l = m+1

        return nums[res]
        