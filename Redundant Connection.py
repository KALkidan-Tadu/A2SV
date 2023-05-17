class UnionFind:
    def __init__(self, size):
        self.rank = defaultdict(int)
        self.rep = {i:i for i in range(1, size)}
        
    def representative(self, x):
        temp = x
        while self.rep[x] != x:
            x = self.rep[x]
        while self.rep[temp] != temp:
            self.rep[temp] = x
            temp = self.rep[temp]
        return x
		
    def union(self, x, y):
        xrep = self.rep[x]
        yrep = self.rep[y]
        if self.rank[xrep] >= self.rank[yrep]:
            self.rep[yrep] = xrep
            if self.rank[xrep] == self.rank[yrep]:
                self.rank[xrep] += 1
        else:
            self.rep[xrep] = yrep
                

    def connected(self, x, y):
        return self.rep[x] == self.rep[y]
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)+1
        graph = UnionFind(n)
        
        for edge in edges:
            root1 = graph.representative(edge[0])
            root2 = graph.representative(edge[1])
            if graph.connected(root1, root2):
                return [edge[0], edge[1]]
            graph.union(edge[0], edge[1])
        
