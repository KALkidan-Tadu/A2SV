class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        cols = []

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.append(row)
                    cols.append(col)
        
        for row in rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0
