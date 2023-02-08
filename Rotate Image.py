class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for col in range(n):
            temp = []
            for row in range(n-1, -1, -1):
                temp.append(matrix[row][col])
            matrix.append(temp)

        for itrn in range(n):
            matrix.pop(0)
        
