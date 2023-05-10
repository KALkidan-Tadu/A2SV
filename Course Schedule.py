class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        depend = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        order = []

        for i in range(len(prerequisites)):
           depend[prerequisites[i][1]].append(prerequisites[i][0])
           indegree[prerequisites[i][0]] += 1
        
        for i in range(numCourses): 
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            node = queue.popleft()
            for course in depend[node]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
            order.append(node)
        if len(order) == numCourses:
            return True
        return False
