class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxSize = 0
        for trip in trips:
            maxSize = max(maxSize, max(trip))
        
        cars = [0]*(maxSize+1)

        for trip in trips:
            cars[trip[1]] += trip[0]
            if trip[2] < maxSize:
                cars[trip[2]] -= trip[0]
        
        for i in range(1, len(cars)):
            cars[i] += cars[i-1]
        for car in cars:
            if car > capacity:
                return False
        return True
