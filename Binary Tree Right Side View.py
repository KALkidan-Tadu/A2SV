# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
        if root == None:
            return []
        traverse(root, 0)
        nums = []
        for arr in answer:
            nums.append(arr[-1])
        return nums
        
        
