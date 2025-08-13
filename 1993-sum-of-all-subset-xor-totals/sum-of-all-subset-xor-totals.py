class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        res = 0

        def dfs(start, ans):
            if start == len(nums):
                nonlocal res
                x = 0
                for a in ans:
                    x ^= a
                res += x

                return
            
            ans.append(nums[start])
            dfs(start+1, ans)
            ans.pop()

            dfs(start+1, ans)

        dfs(0,[])

        return res
