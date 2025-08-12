# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.currentCount = 0
        self.kthValue = None

        def inorder(root, k):
            if root is None:
                return None
            
            inorder(root.left, k)

            if self.currentCount <= k:
                self.currentCount += 1
            else:
                return None

            if self.currentCount == k:
                self.kthValue =  root.val
                return None

            inorder(root.right, k)

            return None

        inorder(root, k)

        return self.kthValue





        