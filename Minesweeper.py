class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0], [-1, -1], [1, -1], [1, 1], [-1, 1]]
        def isBound(row, col):
            return 0<=row<len(board) and 0<=col<len(board[0])
        def count(row, col):
            neighbours = 0
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if isBound(new_row, new_col) and board[new_row][new_col] == "M":
                    neighbours += 1
            return neighbours
        visited = set()
        def dfs(row, col):
            if (row, col) in visited:
                return 
            visited.add((row, col))
            if board[row][col] == "M":
                return 

            neighbours = count(row, col)
            if neighbours == 0:
                board[row][col] = "B"
                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    if isBound(new_row, new_col):
                        dfs(new_row, new_col)
            else:
                board[row][col] = str(neighbours)
                return

        row = click[0]
        col = click[1]
        if board[row][col] == "M":
            board[row][col] = "X"
            return board
        dfs(row, col)
        return board


      
