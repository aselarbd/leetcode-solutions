class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        asending, disending, res =  {0:nums[0]}, {len(nums)-1: nums[-1]}, [0]*len(nums)

        for i in range(1,len(nums)):
            asending[i] = asending[i-1] * nums[i]

        for i in range(len(nums)-2, -1,-1):
            disending[i] = disending[i+1] * nums[i]


        res [0] = disending[1]
        res [-1] = asending[len(nums)-2]

        for i in range(1,len(nums)-1):
            res[i] = asending[i-1] * disending[i+1]

        return res



        