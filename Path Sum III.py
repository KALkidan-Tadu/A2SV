# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0
        total = 0
        sum_ = 0
        d = defaultdict(int)

        def path(node):
            nonlocal total, sum_

            sum_ += node.val
            if sum_ == targetSum:
                total += 1
            total += d[sum_ - targetSum]
            d[sum_] += 1

            if node.left:
                path(node.left)
                d[sum_] -= 1
                sum_ -= node.left.val
            if node.right:
                path(node.right)
                d[sum_] -= 1
                sum_ -= node.right.val
        
        path(root)
        return total

        
