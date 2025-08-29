class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = len(nums)/2
        counter = {}

        for n in nums:
            counter[n] = counter.get(n,0) + 1
            if counter[n]> major:
                return n
        

        