class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        def backTrack(arr, index):
            if index >= n:
                if len(arr) >= 3:
                    return True
                return False
            
            for i in range(index+1, n+1):
                temp = num[index:i]
                if len(arr) < 2 or arr[-1] + arr[-2] == int(temp):
                    if len(temp) > 1 and temp[0] == "0":
                        break
                    arr.append(int(temp))
                    if backTrack(arr, i):
                        return True
                    arr.pop()
            return False
        return backTrack([], 0)
