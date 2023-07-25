class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        directions = [[1,-1], [1, 0], [1,1]]

        def isBound(row, col, n):
            if 0<=row<n and 0<= col < n:
                return True
            return False

        for i in range(n-2, -1, -1):
            for j in range(n):
                val = pow(10,5)
                for d in directions:
                    newRow = i + d[0]
                    newCol = j + d[1]
                    if isBound(newRow, newCol, n):
                        val = min(val, matrix[newRow][newCol])
                matrix[i][j] += val
                
        return min(matrix[0])

                
