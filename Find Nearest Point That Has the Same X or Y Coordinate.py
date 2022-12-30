class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        index = -1
        minimum = 10000
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                if minimum > (abs(x-points[i][0]) + abs(y-points[i][1])):
                    minimum = abs(x-points[i][0]) + abs(y-points[i][1])
                    index = i
        return index
