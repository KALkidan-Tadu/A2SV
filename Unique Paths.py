class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        val = defaultdict(int)
        val[(m-1, n-1)] = 1
        def isbound(row, col):
            return 0 <= row< m and 0<= col < n
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if isbound(i-1, j):
                    val[(i-1, j)] += val[(i, j)]
                if isbound(i, j-1):
                    val[(i, j-1)] += val[(i, j)]
        
        return val[(0,0)]
