# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        path = defaultdict(list)
        visited = set([target.val])
        queue = deque([target.val])
        def traverse(node):
            if node == None:
                return 
            if node.left:
                path[node.val].append(node.left.val)
                path[node.left.val].append(node.val)
                traverse(node.left)
            if node.right:
                path[node.val].append(node.right.val)
                path[node.right.val].append(node.val)
                traverse(node.right)
        traverse(root)
        distance = 0
        while queue:
            if distance == k:
                return list(queue)
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                for n in path[node]:
                    if n not in visited:
                        visited.add(n)
                        queue.append(n)
            distance += 1

        return []
