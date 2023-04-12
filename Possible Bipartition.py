class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        likes, colors = defaultdict(list), {}
        for i,j in dislikes : likes[i].append(j), likes[j].append(i)
        
        def dfs(i, col):
            if i in colors :
                 return colors[i] == col
            colors[i] = col
            return all(dfs(j, not col) for j in likes[i])

        return all(dfs(i, True) for i in range(1,n+1) if i not in colors)
        
