class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]: 
        answer = []
        def backTrack(arr, num):
            if len(arr) == k:
                answer.append(arr.copy())
                return
            
            for i in range(num, n+1):
                arr.append(i)
                backTrack(arr, i+1)
                arr.pop()
        
        backTrack([], 1)
        return answer
