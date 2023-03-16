class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        prefix = grid[0].copy()
        suffix = grid[1].copy()
        n = len(grid[0])

        for index in range(1, n):
            prefix[index] += prefix[index-1]
        
        for index in range(n-2, -1, -1):
            suffix[index] += suffix[index+1]
        
        answer = inf
        score = 0

        for index in range(n):
            score = max(prefix[n-1] - prefix[index], suffix[0] - suffix[index])
            answer = min(answer, score)
        
        return answer
        
