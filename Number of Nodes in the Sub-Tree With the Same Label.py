class Solution:
    def countSubTrees(self, n: int, edges: list[list[int]], labels: str) -> list[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        answer = [0] * n

        def dfs(vertex, parent, count) -> None:
            before = count[labels[vertex]]

            for adjacent in graph[vertex]:
                if adjacent != parent:
                    dfs(adjacent, vertex, count)

            count[labels[vertex]] += 1
            answer[vertex] = count[labels[vertex]] - before

        dfs(0, 0, Counter())
        return answer
   
