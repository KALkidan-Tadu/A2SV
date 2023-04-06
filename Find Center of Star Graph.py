class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        star = -1
        d = defaultdict(int)

        for e in edges:
            d[e[0]] += 1
            d[e[1]] += 1
        
        n = len(edges)
        for k in d.keys():
            if d[k] == n:
                return k
