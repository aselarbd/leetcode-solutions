class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(start, tot, ans):

            if tot == target:
                res.append(ans[:])
                return
            
            if start == len(candidates) or tot > target:
                return

            # Add element
            ans.append(candidates[start])
            dfs(start, tot+candidates[start], ans)
            ans.pop()

            # Not add element
            dfs(start+1, tot, ans)

        dfs(0,0,[])

        return res
        