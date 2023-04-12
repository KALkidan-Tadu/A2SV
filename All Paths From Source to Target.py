class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        dest = len(graph) - 1
        path = []

        def dfs(node, arr):
            if node == dest:
                arr.append(node)
                path.append(arr.copy())
                return
            arr.append(node)

            for num in graph[node]:
                dfs(num, arr)
                arr.pop()
        for g in graph[0]:
            dfs(g, [0])
        return path

