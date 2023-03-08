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

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        self.traverse(root, nums)
        d = defaultdict(int)
        maxFreq = -1
        for num in nums:
            d[num] += 1
            maxFreq = max(maxFreq, d[num])
        answer = []
        nums = list(set(nums))
        for num in nums:
            if d[num] == maxFreq:
                answer.append(num)
        return answer
