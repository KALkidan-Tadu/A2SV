# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        seen = deque()
        seen.append((root, 1))
        maxLen = 1 

        while seen:
            n = len(seen)
            for i in range(n):
                temp = seen.popleft()
                node = temp[0]
                index = temp[1]

                if node.left:
                    seen.append((node.left, index*2))
                if node.right:
                    seen.append((node.right, index*2+1))
            if len(seen):
                maxLen = max(maxLen, seen[-1][1] - seen[0][1] + 1)
        
        return maxLen

        
