# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(root1, root2):
            if root1 is None and root2 is None:
                return None
            if root1 is None:
                return root2
            if root2 is None:
                return root1
            
            left =  dfs(root1.left, root2.left)
            right = dfs(root1.right, root2.right)

            return TreeNode(val=root1.val+root2.val, left=left, right=right)

        return dfs(root1,root2)


        