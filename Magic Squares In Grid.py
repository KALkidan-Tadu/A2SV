class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        magicSquares = 0
        nums = set((1,2,3,4,5,6,7,8,9))

        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                row1 = grid[row][col]+grid[row][col+1]+grid[row][col+2]
                row2 = grid[row+1][col]+grid[row+1][col+1]+grid[row+1][col+2] 
                row3 = grid[row+2][col]+grid[row+2][col+1]+grid[row+2][col+2]             
                col1 = grid[row][col]+grid[row+1][col]+grid[row+2][col]
                col2 = grid[row][col+1]+grid[row+1][col+1]+grid[row+2][col+1]
                col3 = grid[row][col+2]+grid[row+1][col+2]+grid[row+2][col+2]
                diag1 = grid[row][col]+grid[row+1][col+1]+grid[row+2][col+2]
                diag2 = grid[row][col+2]+grid[row+1][col+1]+grid[row+2][col]
                
                if row1==row2 and row1==row3 and row1==col1 and row1==col2 and row1==col3 and row1==diag1 and row1==diag2:
                    if set((grid[row][col],grid[row][col+1],grid[row][col+2],grid[row+1][col],grid[row+1][col+1],grid[row+1][col+2],grid[row+2][col],grid[row+2][col+1],grid[row+2][col+2],)) == nums:
                        magicSquares += 1
        
        return magicSquares
