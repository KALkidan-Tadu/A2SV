class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        now = 0
        heap1 = []
        heap2 = []
        order = []
        for i in range(len(tasks)):
            heappush(heap1, (tasks[i][0], tasks[i][1], i))
        
        while heap1 or heap2:
            while heap1 and heap1[0][0] <= now:
                start, length, index = heappop(heap1)
                heappush(heap2, (length, index))
            
            if heap2:
                length, index = heappop(heap2)
                order.append(index)
                now += length
            elif heap1:
                now = heap1[0][0]
        
        return order

        
