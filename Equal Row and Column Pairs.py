class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = defaultdict(int)
        equalPairs = 0

        for row in grid:
            rows[tuple(row)] += 1
        
        for col in range(len(grid[0])):
            column = []
            for row in range(len(grid)):
                column.append(grid[row][col])
            equalPairs += rows[tuple(column)]
            
        return equalPairs
