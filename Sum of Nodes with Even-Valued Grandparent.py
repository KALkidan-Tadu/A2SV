# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        sum_ = 0
        
        def traverse(grand, par, node):
            nonlocal sum_
            if grand.val % 2 == 0:
                    sum_ += node.val
            if node.left == None and node.right == None:
                return
            if node.left:
                traverse(par, node, node.left)
            if node.right:
                traverse(par, node, node.right)

        if root == None:
                return 0
        if root.left and root.left.left:
            traverse(root, root.left, root.left.left)
        if root.left and root.left.right:
            traverse(root, root.left, root.left.right)
        if root.right and root.right.left:
            traverse(root, root.right, root.right.left)
        if root.right and root.right.right:
            traverse(root, root.right, root.right.right)
        return sum_
