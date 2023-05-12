class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        answer = []
        queue = deque()
        for rich in richer:
            graph[rich[0]].append(rich[1])
            indegree[rich[1]] += 1
        
        for i in range(len(quiet)):
            answer.append(i)
            if indegree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                if quiet[answer[node]] < quiet[answer[child]]:
                    answer[child] = answer[node]
                indegree[child] -= 1
                if indegree[child] == 0:
                    queue.append(child)

        return answer
        
