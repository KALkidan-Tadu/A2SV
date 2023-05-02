class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row_len, col_len = len(maze), len(maze[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def check(row, col):
            return 0<=row<len(maze) and 0<=col<len(maze[0])and maze[row][col] == "." and (row, col) not in visited
        
        queue = deque([(entrance[0], entrance[1])])
        visited = {(entrance[0], entrance[1])}
        count = 0

        while queue:
            length = len(queue)
            for _ in range(length):
                row, col = queue.popleft()
                print(row, col)
                if (row in [0, row_len -1] or col in [0, col_len-1]) and(row != entrance[0] or col != entrance[1]):
                    return count
                for d in directions:
                    new_row = row + d[0]
                    new_col = col + d[1]
                    if check(new_row, new_col):
                        queue.append((new_row,new_col))
                        visited.add((new_row, new_col))
            count += 1
        return -1
