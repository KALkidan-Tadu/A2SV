class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        maxPath = -1

        for road in roads:
            d[road[0]].append(road[1])
            d[road[1]].append(road[0])

        for i in range(n):
            for j in range(i+1, n):
                path = len(d[i]) + len(d[j])
                if i in d[j]:
                    path -= 1
                maxPath = max(maxPath, path)

        return maxPath 
