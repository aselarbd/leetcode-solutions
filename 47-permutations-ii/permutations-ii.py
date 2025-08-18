class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n, res = len(nums), []
        nums.sort()
        used = [False]*n

        def dfs(s,ans):
            if s == n:
                res.append(ans[:])
                return

            for i in range(n):

                if used[i]:
                    continue

                if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                ans.append(nums[i])
                used[i] = True

                dfs(s+1, ans)

                ans.pop()
                used[i] = False

        dfs(0,[])
        return res
        