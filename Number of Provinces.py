class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        comps = 0
        d = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    d[i].append(j)

        def dfs(val):
            if val not in visited:
                visited.add(val)
                for v in d[val]:
                    if v not in visited:
                        dfs(v)
        
        for k in d.keys():
            if k not in visited:
                comps += 1
                dfs(k)
        
        return comps
