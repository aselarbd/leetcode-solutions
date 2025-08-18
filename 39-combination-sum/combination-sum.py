class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(candidates, reaminder, ans):

            if reaminder == 0:
                res.append(ans[:])
                return

            for i,c in enumerate(candidates):
                if i >0 and candidates[i-1] == c: continue

                if reaminder - c >= 0:
                    ans.append(c)
                    dfs(candidates[i:], reaminder - c, ans)
                    ans.pop()

        candidates.sort()
        dfs(candidates, target, [])

        return res
        