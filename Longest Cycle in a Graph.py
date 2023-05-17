class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        indegree = defaultdict(int)
        outdegree = defaultdict(int)
        graph = defaultdict(list)

        for index in range(len(edges)):
            if edges[index] != -1:
                indegree[edges[index]] += 1
        queue = deque()
        visited = set()

        for i in range(len(edges)):
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            visited.add(node)
            if edges[node] != -1 and edges[node] not in visited:
                indegree[edges[node]] -= 1
                if indegree[edges[node]] == 0:
                    queue.append(edges[node])
        if len(visited) == len(edges):
            return -1
        answer = -1
        for i in range(len(edges)):
            if i not in visited:
                visited.add(i)
                neighbour = edges[i]
                length = 1
                while neighbour != i:
                    length += 1
                    visited.add(neighbour)
                    neighbour = edges[neighbour]
                answer = max(answer, length)
        return answer
