# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self, root, arr):
        if root == None:
            return None
        self.traverse(root.left, arr)
        arr.append(root.val)
        self.traverse(root.right, arr)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        self.traverse(root, nums)
        return nums[k-1]
