# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.goodNodeCount = 0

        def dfs(root, val):

            if root is None:
                return None
            
            if root.val >= val:
                self.goodNodeCount += 1
            
            new_max = max(val, root.val)
            dfs(root.left, new_max)
            dfs(root.right, new_max)

            return None

        dfs(root, root.val)

        return self.goodNodeCount