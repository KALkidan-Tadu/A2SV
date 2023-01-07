class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        afterMove = []
        indices = []
        for index in range(len(boxes)):
            if boxes[index] == '1':
                indices.append(index)
        
        for index in range(len(boxes)):
            moves = 0
            for i in indices:
                moves += abs(index-i)
            afterMove.append(moves)
        
        return afterMove
