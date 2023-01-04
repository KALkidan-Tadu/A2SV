class Solution:
    def checkWin(self, board, val):
        for i in range(3):
            if board[i][0]==val and board[i][1]==val and board[i][2]==val:
                return True
            if board[0][i]==val and board[1][i]==val and board[2][i]==val:
                return True
            if i==0 and board[i][i]==val and board[i+1][i+1]==val and board[i+2][i+2]==val:
                return True
            if i==0 and board[i][i+2]==val and board[i+1][i+1]==val and board[i+2][i]==val:
                return True
            return False

    def validTicTacToe(self, board: List[str]) -> bool:
        x = 0
        o = 0
        
        for word in board:
            for letter in word:
                if letter=='X':
                    x += 1
                elif letter == 'O':
                    o += 1
        if x==o:
            if self.checkWin(board, 'X'):
                return False
            return True

        elif x==o+1:
            if self.checkWin(board, 'O'):
                return False
            return True
        return False
