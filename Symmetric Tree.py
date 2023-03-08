# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEqual(self, root1, root2):
        if root1 == None or root2 == None:
            if root1 or root2:
                return False
            return True
        if root1.val != root2.val:
            return False
        return self.isEqual(root1.left, root2.right) and self.isEqual(root1.right, root2.left)
   
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isEqual(root.right, root.left)
