class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l,r,res = 0,len(nums)-1,-1

        while l<=r:
            m = (l+r)//2

            if nums[m]>=target:
                res = m
                r = m-1
            else:
                l = m+1
        return res if res !=-1 else len(nums)
        