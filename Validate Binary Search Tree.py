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

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        self.traverse(root, ans)
        nums = [] + ans
        nums.sort()
        if nums == ans:
            nums = set(nums)
            if len(nums) == len(ans):
                return True
            return False
        return False
