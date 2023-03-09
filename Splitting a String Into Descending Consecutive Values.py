class Solution:
    def splitString(self, s: str) -> bool:
        
        answer = []
        def backTrack(index):
            if len(s) == index:
                if len(answer) >= 2:
                    return True
                return False

            for i in range(index, len(s)):
                num = int(s[index : i+1])
                if len(answer) == 0 or answer[-1] - num == 1:
                    answer.append(num)
                    if backTrack(i+1):
                        return True
                    answer.pop()
            return False

        return backTrack(0)
