# UnionFind class
class UnionFind:
    def __init__(self, n):
        self.rank = defaultdict(int)
        self.rep = {i:i for i in range(n)}
        self.size = [1] * n
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
            self.size[xrep] += self.size[yrep]
            if self.rank[xrep] == self.rank[yrep]:
                self.rank[xrep] += 1
        else:
            self.rep[xrep] = yrep
            self.size[yrep] += self.size[xrep]   

    def connected(self, x, y):
        return self.rep[x] == self.rep[y]

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        graph =  UnionFind(n)
        parents = set()
        for i in range(n-1):
            for j in range(i+1, n):
                if (stones[i][0] == stones[j][0] or stones[j][1] == stones[i][1]) and graph.connected(graph.representative(i) , graph.representative(j)) == False:
                    graph.union(graph.representative(i), graph.representative(j))
        
        for i in range(n):
            parents.add(graph.representative(i))
        
        total = 0
        parents = list(parents)
        for parent in parents:
            total += (graph.size[parent] - 1)
        return total
