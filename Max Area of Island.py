class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()

        def isBound(row, col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])

        def dfs(row, col):
            nonlocal land
            if (row, col) not in visited and grid[row][col] == 1:
                visited.add((row, col))
                land += 1

            for dir in directions:
                new_row = row + dir[0]
                new_col = col + dir[1]
                if isBound(new_row, new_col) and grid[new_row][new_col ] == 1 and (new_row, new_col) not in visited:
                    dfs(new_row, new_col)

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visited:
                    land = 0
                    dfs(i, j)
                    max_area = max(max_area, land)

        return max_area

