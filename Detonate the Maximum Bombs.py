class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        connected = defaultdict(list)
        for bomb in range(len(bombs)):
            r = bombs[bomb][2]
            for b in range(len(bombs)):
                if bomb != b:
                    x = pow((bombs[bomb][0]-bombs[b][0]), 2)
                    y = pow((bombs[bomb][1]-bombs[b][1]), 2)
                    d = pow((x+y), 0.5)
                    if r >= d:
                        connected[bomb].append(b)
                        
        maxBomb = 0
        def dfs(node, total, visited):
            if node in visited:
                return len(visited)
            visited.add(node)
            for n in connected[node]:
                dfs(n, total, visited)
            return len(visited)
        
        for i in range(len(bombs)):
            visited = set()
            maxBomb = max(maxBomb, dfs(i, 0, visited))
        
        return maxBomb
