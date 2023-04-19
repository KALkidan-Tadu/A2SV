class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        notAllowed = set()
        directions = [[0,1], [0,-1], [-1,0], [1,0]]

        def isBound(row, col):
            return 0 <= row <= len(board)-1 and 0 <= col <= len(board[0])-1
        def restricted(row, col):
            if (row, col) not in notAllowed:
                notAllowed.add((row, col))

                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    if isBound(new_row, new_col) and board[new_row][new_col] == "O":
                        restricted(new_row, new_col)
        def dfs(row, col):
            if (row, col) not in visited and (row, col) not in notAllowed:
                visited.add((row, col))
                board[row][col] = "X"

                for direc in directions:
                    new_row = row + direc[0]
                    new_col = col + direc[1]
                    if isBound(new_row, new_col) and board[new_row][new_col] == "O":
                        dfs(new_row, new_col)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if (r == 0 or c == 0 or r == len(board)-1 or c == len(board[0])-1) and board[r][c] == "O" and (r,c) not in notAllowed:
                    restricted(r,c)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i,j) not in visited and (i,j) not in notAllowed:
                    dfs(i, j)
