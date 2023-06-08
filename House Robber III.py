# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memo = {}
        
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            
            if root == None:
                return 0
            
            if root not in self.memo:
                
                pick = 0
                if root.left:
                    pick += dfs(root.left.left) + dfs(root.left.right)

                if root.right:
                    pick += dfs(root.right.left) + dfs(root.right.right)

                pick += root.val 
                not_pick = dfs(root.left) + dfs(root.right)
            
                self.memo[root] = max(pick, not_pick)
                
            return self.memo[root]
        
        return dfs(root)
        
