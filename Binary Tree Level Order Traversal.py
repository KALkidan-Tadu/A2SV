# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        def traverse(root, level):
            nonlocal answer

            if root:
                if len(answer) > level:
                    answer[level].append(root.val)
                else:
                    answer.append([root.val])
                traverse(root.left, level+1)
                traverse(root.right, level+1)

            return 
        traverse(root, 0)
        return answer
            
                
                  
                  
                
            
        
