class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        prev = values[0] - 1
        answer = -1
        n = len(values)

        for i in range(1, n):
            answer = max(answer, prev+values[i])
            prev = max(prev-1, values[i]-1)
        
        return answer



