# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque([root])
        averages = []

        while queue:
            length = len(queue)
            sum_ = 0
            
            for i in range(length):
                node = queue.popleft()
                sum_ += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            averages.append(sum_/ length)
        
        return averages
        
