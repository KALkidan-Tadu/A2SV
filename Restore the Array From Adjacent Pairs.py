class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        visited = set()
        indegree = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        nums = []
        for adjacent in adjacentPairs:
            indegree[adjacent[0]] += 1
            indegree[adjacent[1]] += 1
            graph[adjacent[0]].append(adjacent[1])
            graph[adjacent[1]].append(adjacent[0])
        for key in indegree.keys():
            if indegree[key] == 1:
                queue.append(key)
                visited.add(key)
                break
        
        while queue:
            num = queue.popleft()
            nums.append(num)
            for child in graph[num]:
                if child not in visited:
                    indegree[child] -= 1
                    if indegree[child] <= 1:
                        queue.append(child)
                        visited.add(child)
        return nums
