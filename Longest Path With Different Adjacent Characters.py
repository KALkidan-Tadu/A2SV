class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)

        for i in range(len(parent)):
            if parent[i] != -1:
                graph[parent[i]].append(i)
                graph[i].append(parent[i])

        @cache
        def dfs(node, parent):
            maxLen = 1
            for neighbor in graph[node]:
                if neighbor == parent: continue
                if s[neighbor] != s[node]:
                    maxLen = max(maxLen, dfs(neighbor, node) + 1)
            return maxLen
        return max(dfs(i, -1) for i in range(len(parent)))
