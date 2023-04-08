"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        dep = 0
        if root == None:
            return 0
        if root.children:
            dep = max(self.maxDepth(n) for n in root.children)
        return dep + 1 
        
