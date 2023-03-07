# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, arr):
        if root == None:
            arr.append(-1)
            return 
        arr.append(root.val)
        self.traverse(root.left, arr)
        self.traverse(root.right, arr)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []
        self.traverse(p, tree1)
        self.traverse(q, tree2)

        if tree1 == tree2:
            return True
        return False
