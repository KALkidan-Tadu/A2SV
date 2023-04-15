class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [[0,1], [0, -1], [1, 0], [-1, 0]]
        subislands = 0
        def isBound(row, col):
            return 0<=row<len(grid1) and 0<=col<len(grid1[0])

        visited = set()

        def dfs(row, col):
            visited.add((row, col))
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if isBound(new_row, new_col) and (new_row, new_col) not in visited and grid2[row][col]:
                    dfs(new_row, new_col)

        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if (row, col) not in visited and grid1[row][col] == 0 and grid2[row][col] == 1:
                    dfs(row, col)

        for row in range(len(grid1)):
            for col in range(len(grid1[0])):
                if (row, col) not in visited and grid2[row][col] == 1:
                    subislands += 1
                    dfs(row, col)

        return subislands
