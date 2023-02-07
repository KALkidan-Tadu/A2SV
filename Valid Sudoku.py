class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            nums = {}
            for col in range(len(board[0])):
                if board[row][col] != "." and board[row][col] not in nums:
                    nums[board[row][col]] = 1
                elif board[row][col] != "." and board[row][col] in nums:
                    return False
        for col in range(len(board[0])):
            nums = {}
            for row in range(len(board)):
                if board[row][col] != "." and board[row][col] not in nums:
                    nums[board[row][col]] = 1
                elif board[row][col] != "." and board[row][col] in nums:
                    return False
        
        for i in range(3):
            for j in range(3):
                nums = {}
                for x in range(i*3, i*3+3):
                    for y in range(j*3, j*3+3):
                        if board[x][y] != '.':
                            if board[x][y] not in nums:
                                nums[board[x][y]] = 1
                            else:
                                return False
        return True
