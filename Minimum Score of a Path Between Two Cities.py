class UnionFind:
    def __init__(self, size):
        self.roots = [i for i in range(size)]
        self.rank = [0 for _ in range(size)]

    def find(self, x) -> int:
        if x != self.roots[x]:
            self.roots[x] = self.find(self.roots[x])

        return self.roots[x]

    def connected(self, x, y) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x, y) -> None:
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        x_rank = self.rank[x_root]
        y_rank = self.rank[y_root]

        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1

        if x_rank > y_rank:
            self.roots[y_root] = x_root
        else:
            self.roots[x_root] = y_root

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = UnionFind(n + 1)
        
        for road in roads:
            graph.union(road[0], road[1])
        
        answer = inf
        
        for road in roads:
            if graph.connected(road[0], 1):
                answer = min(answer, road[2])
        
        return answer
            
        
        
        
