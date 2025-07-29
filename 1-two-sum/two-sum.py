class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        locations = {}

        for i,n in enumerate(nums):
            rem = target - n
            if rem in locations:
                return [i, locations[rem]]
            else:
                locations[n] = i
        