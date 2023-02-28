class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        index = 0
        time = 0
        while tickets[k] > 0:
            if tickets[index%len(tickets)] > 0:
                tickets[index%len(tickets)] -= 1
                time += 1
            index += 1
        
        return time


            
