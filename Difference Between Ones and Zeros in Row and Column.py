class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowSum1 = []
        rowSum0 = []
        colSum1 = []
        colSum0 = []
        answer = []
        for row in range(len(grid)):
            r0, r1 = 0, 0
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    r1 += 1
                elif grid[row][col] == 0:
                    r0 += 1
            rowSum0.append(r0)
            rowSum1.append(r1)
        for col in range(len(grid[0])):
            c0, c1 = 0, 0
            for row in range(len(grid)):
                if grid[row][col] == 1:
                    c1 += 1
                elif grid[row][col] == 0:
                    c0 += 1
            colSum1.append(c1)
            colSum0.append(c0)

        for row in range(len(grid)):
            temp = []
            for col in range(len(grid[0])):
                temp.append(rowSum1[row] + colSum1[col] - rowSum0[row] - colSum0[col]) 
            answer.append(temp)
        
        return answer
