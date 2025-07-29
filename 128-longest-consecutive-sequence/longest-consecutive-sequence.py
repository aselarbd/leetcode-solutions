class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet, longest = set(nums), 0

        for n in numSet:
            if not n-1 in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest,length)
        return longest      