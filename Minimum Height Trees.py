class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:  
        if len(edges) == 0:
            return [0]
        graph = defaultdict(list)
        height = defaultdict(int)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            height[edge[0]] += 1
            height[edge[1]] += 1
        
        queue = deque()
        for key in height.keys():
            if height[key] == 1:
                queue.append(key)
        while n > 2:
            length = len(queue)
            n -= length
            for _ in range(length):
                node = queue.popleft()
                for child in graph[node]:
                    height[child] -= 1
                    if height[child] == 1:
                        queue.append(child)
        return queue
                        


