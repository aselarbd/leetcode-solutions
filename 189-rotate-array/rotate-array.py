class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k> len(nums):
            k= k%len(nums)

        nums[:k], nums[k:] = nums[-k:], nums[:len(nums)-k]
        