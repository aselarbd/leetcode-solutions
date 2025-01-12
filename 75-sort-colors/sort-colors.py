class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k=0

        for i in range(len(nums)):
            if nums[i] ==0:
                nums[k],nums[i] = nums[i],nums[k]
                k+=1
        
        for i in range(len(nums)):
            if nums[i] ==1:
                nums[k],nums[i] = nums[i],nums[k]
                k+=1