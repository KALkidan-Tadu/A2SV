class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0]*(len(s)+1)

        for shift in shifts:
            if shift[2] == 1:
                prefix[shift[0]] += 1
                prefix[shift[1]+1] -= 1
            else:
                prefix[shift[0]] -= 1
                prefix[shift[1]+1] += 1
        
        for i in range(1, len(prefix)):
            prefix[i] += prefix[i-1]
                
        s = list(s)
        for index in range(len(s)):
            s[index] = chr((ord(s[index]) - 97 + prefix[index]) % 26 + 97)
        return "".join(s)
        
