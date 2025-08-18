class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res, nums =  [], [i for i in range(1, n+1)]

        def dfs(start,ans):

            if len(ans) == k:
                res.append(ans[:])
                return
            
            for i in range(start,n):
                if len(ans) < k:
                    ans.append(nums[i])
                    dfs(i+1, ans)
                    ans.pop()

            
        dfs(0,[])

        return res        
        
        