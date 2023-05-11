class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue = deque()
        indegree = defaultdict(int)
        path = defaultdict(list)
        answer = []
        index = 0
        for gra in graph:
            if len(gra) == 0:
                queue.append(index)
            else:
                for g in gra:
                    path[g].append(index)
                indegree[index] = len(gra)
            index += 1
        
        while queue:
            node = queue.popleft()
            answer.append(node)
            for p in path[node]:
                indegree[p] -= 1
                if indegree[p] == 0:
                    queue.append(p)
        answer.sort()
        return answer
      
