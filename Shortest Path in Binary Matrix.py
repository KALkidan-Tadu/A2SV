class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        visited = set([(0, 0)])
        queue = deque([(0,0)])
        directions = [[-1,-1],  [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        def check(row, col):
            return 0 <= row < n and 0<= col < n and (row, col) not in visited and grid[row][col] == 0
        distance = 1
        while queue:
            length = len(queue)
            for i in range(length):
                row, col = queue.popleft()
                if row == n-1 and col == n-1:
                    return distance
                for direct in directions:
                    new_row = row + direct[0]
                    new_col = col + direct[1]
                    if check(new_row, new_col):
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
            distance += 1
        return -1
        
