class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_ind = {}

        for i,n in enumerate(nums):
            nums_ind[n]=i
        
        for i,n in enumerate(nums):
            left = target - n
            if left in nums_ind and i != nums_ind[left]:
                return [i,nums_ind[left]]