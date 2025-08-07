class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        ans, summation, left = len(nums)+1,0,0

        for right in range(len(nums)):
            summation += nums[right]

            while summation >= target:
                ans = min(ans, right-left+1)
                summation -= nums[left]
                left += 1

        return ans if ans != len(nums)+1 else 0


        