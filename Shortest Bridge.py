class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions =  [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()
        queue = deque()
        islands = deque()
        def check(row, col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    queue.append((i, j))
                    visited = set([(i, j)])
                    islands.append((i, j))
                    break
            if len(queue):
                break
        while queue:
            row, col = queue.popleft()
            for d in directions:
                new_row = row + d[0]
                new_col = col + d[1]
                if check(new_row, new_col) and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
                    islands.append((new_row, new_col))

        count = 0
        while islands:
            length = len(islands)
            for _ in range(length):
                r, c = islands.popleft()
                for d in directions:
                    new_r = r + d[0]
                    new_c = c + d[1]
                    if check(new_r, new_c) and (new_r, new_c) not in visited:
                        if grid[new_r][new_c] == 1:
                            return count
                        visited.add((new_r, new_c))
                        islands.append((new_r, new_c))
            count += 1  
