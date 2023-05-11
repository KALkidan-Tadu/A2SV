class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        conn = [set() for _ in range(n)]
        indegree = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        for edge in edges:
            graph[edge[0]].append(edge[1])
            indegree[edge[1]] += 1
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            for child in graph[node]:
                conn[child].add(node)
                conn[child].update(conn[node])
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
        
        conn = [sorted(list(a)) for a in conn]
        return conn

        
