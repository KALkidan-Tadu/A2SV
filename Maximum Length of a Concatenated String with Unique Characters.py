class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxLen = 0

        def backTrack(s, index):
            nonlocal maxLen

            if index >= len(arr):
                return
            
            for i in range(index, len(arr)):
                s.append(arr[i])
                word = "".join(s)
                if len(set(word)) == len(word):
                    maxLen = max(maxLen, len(word))
                    backTrack(s, i+1)
                s.pop()

        backTrack([], 0)
        return maxLen
        
