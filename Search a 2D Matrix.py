class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        while row < len(matrix) and target > matrix[row][0]:
            row += 1

        if row<len(matrix) and matrix[row][0] == target:
            return True
        else:
            row -= 1

        col = 1
        while col<len(matrix[0]):
            if matrix[row][col] == target:
                return True
            col += 1
        
        return False
