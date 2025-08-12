# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        minV, maxV = min(p.val, q.val), max(p.val,q.val)

        def dfs(root, minV, maxV):

            if root is None:
                return None

            if root.val < minV:
                return dfs(root.right, minV, maxV)
            elif root.val > maxV:
                return dfs(root.left, minV, maxV)
            else:
                return root
        
        return dfs(root, minV, maxV)