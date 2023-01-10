class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiral = []
        row = len(matrix)
        col = len(matrix[0])
        total = row*col
        rt, rb, lt, lb = col-1, row-1, 1, 0
        i, j = 0, 0
        
        while total:
            while j<=rt and total>0:
                spiral.append(matrix[i][j])
                j += 1
                total -= 1
            i += 1
            j -= 1
            if total == 0:
                break
            
            while i<=rb and total>0:
                spiral.append(matrix[i][j])
                i += 1
                total -= 1
            i -= 1
            j -= 1 
            if total == 0:
                break

            while j>=lb and total>0:
                spiral.append(matrix[i][j])
                j -= 1
                total -= 1
            j += 1
            i -= 1
            if total == 0:
                break

            while i >= lt and total>0:
                spiral.append(matrix[i][j])
                i -= 1
                total -= 1
            i += 1
            j += 1
            rt -= 1
            rb -= 1
            lt += 1
            lb += 1
            
        return spiral
