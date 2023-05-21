# UnionFind class
class UnionFind:
    def __init__(self, size):
        self.rank = defaultdict(int)
        self.rep = {i:i for i in range(size)}
        
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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = UnionFind(len(points))
        def calculate(x, y):
            return abs(x[0]-y[0]) + abs(x[1] - y[1])
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                edges.append((calculate(points[i], points[j]), i, j))

        edges.sort()
        answer = 0
        for cost, x, y in edges:
            if graph.connected(graph.representative(x), graph.representative(y)) == False:
                answer += cost
                graph.union(x,y)
        
        return answer
