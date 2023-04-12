# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        totalSum = 0

        def dfs(node, arr):
            nonlocal totalSum
            if node == None:
                return
            
            arr.append(str(node.val))

            if node.left == None and node.right==None: 
                s = "".join(arr)
                if len(s) > 0:
                    totalSum += int(s)
                return

            if node.left:
                dfs(node.left, arr)
                arr.pop()
            if node.right:
                dfs(node.right, arr)
                arr.pop()
                
        dfs(root, [])
        return totalSum
