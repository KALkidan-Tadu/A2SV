class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        answer = []

        for i in range(len(position)):
           cars.append((position[i], speed[i]))
        cars.sort()
        for c in cars:
            time = (target-c[0])/c[1]
            while answer and answer[-1] <= time:
                answer.pop()
            answer.append(time)
        return len(answer) 


        
        
        
