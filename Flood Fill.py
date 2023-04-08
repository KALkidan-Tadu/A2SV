class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()
        val = image[sr][sc]
        def inbound(row, col):
            return (0 <= row < len(image) and 0 <= col < len(image[0]))
        def dfs(i, j):
            nonlocal val
            if (i,j) in visited:
                return
            image[i][j] = color
            visited.add((i,j))
            for d in directions:
                new_row = i + d[0]
                new_col =  j + d[1]
                if inbound(new_row, new_col) and image[new_row][new_col] == val:
                    image[new_row][new_col] = color
                    dfs(new_row, new_col)
        dfs(sr, sc)
        return image
            
