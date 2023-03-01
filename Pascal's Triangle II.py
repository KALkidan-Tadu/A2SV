class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        answer = [1]
        prev = self.getRow(rowIndex-1)
        for i in range(1, rowIndex):
            answer.append(prev[i] + prev[i-1])
        answer.append(1)

        return answer

            


        
        
    
        
        
        
