class Solution:
    def findMax(self, mat, i, j):
        maxNum = -1
        for row in range(i, i+3):
            for col in range(j, j+3):
                maxNum = max(maxNum, mat[row][col])
        return maxNum

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        localMax = []

        for row in range(len(grid)-2):
            l = []
            for col in range(len(grid[0])-2):
                l.append(self.findMax(grid, row, col))
            localMax.append(l)
        
        return localMax

