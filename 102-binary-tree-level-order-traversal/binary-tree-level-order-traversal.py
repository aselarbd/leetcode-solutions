# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        self.levels = defaultdict(list)

        def dfs(root, h):
            if root is None:
                return None

            self.levels[h].append(root.val)
            
            dfs(root.left, h+1)
            dfs(root.right, h+1)

            return None
        
        dfs(root, 0)

        return [self.levels[h] for h in self.levels.keys()]



        