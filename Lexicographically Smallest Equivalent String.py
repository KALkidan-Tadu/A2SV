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
        if y >= x:
            self.rep[yrep] = xrep
            # if self.rank[xrep] == self.rank[yrep]:
            #     self.rank[xrep] += 1
        else:
            self.rep[xrep] = yrep
                

    def connected(self, x, y):
        return self.rep[x] == self.rep[y]
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = UnionFind(26)
        for index in range(len(s1)):
            a = ord(s1[index]) - 97
            b = ord(s2[index]) - 97
            graph.union(graph.representative(a), graph.representative(b))
        
        answer = []
        for index in range(len(baseStr)):
            node = ord(baseStr[index]) - 97
            parent = graph.representative(node)
            answer.append(chr(parent + 97))
        
        return "".join(answer)
