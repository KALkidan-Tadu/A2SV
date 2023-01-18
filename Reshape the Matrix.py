class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)*len(mat[0]):
            return mat
        
        reshaped = []
        new_row = []
        row, col, index = 0, 0, 0
        
        while row < len(mat):
            while col<len(mat[row]) and index<c:
                new_row.append(mat[row][col])
                index += 1
                col += 1
            if col == len(mat[0]):
                row += 1
                col = 0
            if index == c:
                reshaped.append(new_row)
                index = 0
                new_row = []

        return reshaped
