class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer = []
        n = len(s)

        def backTrack(arr, index):
            if index == n:
                if len(arr) == 4:
                    answer.append(".".join(arr))
                return 
            
            for i in range(index+1, n+1):
                temp = s[index:i]
                if int(temp) >= 0 and int(temp) <= 255:
                    if len(temp) > 1 and temp[0] == "0":
                        break
                    arr.append(temp)
                else:
                    break
                backTrack(arr, i)
                arr.pop()
        backTrack([], 0)
        return answer
