class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reacheable = [set() for _ in range(numCourses)]
        indegree = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        for pre in prerequisites:
            graph[pre[0]].append(pre[1])
            indegree[pre[1]] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)
                reacheable[child].add(node)
                reacheable[child].update(reacheable[node])

        answer = []
        for query in queries:
            if query[0] in reacheable[query[1]]:
                answer.append(True)
            else:
                answer.append(False)
        
        return answer
