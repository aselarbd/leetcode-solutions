class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter, res, limit = {}, [], len(nums)/3
        for n in nums:
            counter[n] = counter.get(n,0) + 1
            if counter[n]> limit and n not in res:
                res.append(n)
        return res
        