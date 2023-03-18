# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []

        def backTrack(s, node):
            if node.left  == None and node.right == None:
                s.append(str(node.val))
                answer.append("->".join(s))
                return
            
            s.append(str(node.val))
            if node.left:
                backTrack(s.copy(), node.left)
            if node.right:
                backTrack(s.copy(), node.right)
            
        backTrack([], root)
        return answer

