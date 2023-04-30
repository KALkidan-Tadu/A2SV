class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node, parent):
            steps = 0
            for child in adj[node]:
                if child != parent: 
                    steps += dfs(child, node)
            if steps or hasApple[node]:
                return steps + 2 
            return 0
            
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            
        result = dfs(0, None)  
        if result:      
            return result - 2 
        return 0
