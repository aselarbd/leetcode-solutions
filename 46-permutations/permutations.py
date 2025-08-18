class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res,  used = [], [False]*n

        def dfs(start, ans):

            if start >= n:
                res.append(ans[:])
                return

            for i in range(n):
                if not used[i]:

                    ans.append(nums[i])
                    used[i] = True

                    dfs(start+1, ans)

                    ans.pop()
                    used[i] = False
        dfs(0,[])

        return res


        