class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(i, ans):
            if i == len(nums):
                nonlocal res
                res.append(ans[:])
                return
            
            ans.append(nums[i])
            dfs(i+1,ans)
            ans.pop()

            dfs(i+1, ans)
        
        dfs(0,[])

        return res

        
        