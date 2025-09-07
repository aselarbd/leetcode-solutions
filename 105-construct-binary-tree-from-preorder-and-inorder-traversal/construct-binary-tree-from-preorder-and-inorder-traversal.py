# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def dfs(preo, ino):
            if not preo and not ino:
                return None
            
            curr = preo[0]

            ino_ind = ino.index(curr)
            ino_left, ino_right = ino[:ino_ind], ino[ino_ind+1:]

            ino_left_count = len(ino_left)
            preo_left, preo_right =  preo[1:ino_left_count+1], preo[ino_left_count+1:]

            left = dfs(preo_left, ino_left)
            right = dfs(preo_right, ino_right)

            return TreeNode(val=curr, left=left, right=right)
            
        
        return dfs(preorder, inorder)
        