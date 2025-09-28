class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def feasibility(m, nums, k):
            count, curr_sum = 1,0
            for n in nums:
                if curr_sum + n > m:
                    curr_sum = n
                    count += 1
                else:
                    curr_sum += n
            return count <= k

        l,r,res = max(nums), sum(nums), -1

        while l <= r:
            m = (l+r)//2
            if feasibility(m,nums,k):
                res = m
                r = m-1
            else:
                l = m+1
        return res
