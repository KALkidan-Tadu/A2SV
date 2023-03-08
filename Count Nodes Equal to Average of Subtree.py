# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def calculate(root):
            nonlocal result 
            
            if root == None:
                return 0, 0
            leftSum, leftCount = calculate(root.left)
            rightSum, rightCount = calculate(root.right)
            sums = root.val + leftSum + rightSum
            total = 1 + leftCount + rightCount

            if sums//total == root.val:
                result += 1
            
            return sums, total
            
        calculate(root)
        return result

