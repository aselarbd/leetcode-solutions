class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n,0) + 1
        
        for item in counter.items():
            if item[1] > len(nums)/2 :
                return item[0]

        