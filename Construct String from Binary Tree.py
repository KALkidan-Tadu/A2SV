# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        path = []

        def dfs(node):
            if node == None:
                return
            path.append(str(node.val))
            if node.left == None and node.right == None:
                return

            if node.left:
                path.append("(")
                dfs(node.left)
                path.append(")")

            if node.right:
                if node.left == None:
                    path.append("()")
                path.append("(")
                dfs(node.right)
                path.append(")")
        dfs(root)
        return "".join(path)
            
