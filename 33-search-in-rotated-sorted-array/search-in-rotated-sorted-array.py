class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l,r,rot = 0,len(nums)-1, -1

        while l <= r:
            m = (l+r)//2

            if nums[m] <= nums[-1]:
                rot = m
                r = m-1
            else:
                l = m+1

        res = -1 

        if rot > 0 and target <= nums[rot-1] and target >= nums[0]:
            l,r = 0,rot-1
        else:
            l,r = rot, len(nums)-1

        while l <= r:
            m = (l+r)//2

            if nums[m] >= target:
                res =  m
                r = m-1
            else:
                l = m+1
        
        return res if nums[res] == target else -1
        