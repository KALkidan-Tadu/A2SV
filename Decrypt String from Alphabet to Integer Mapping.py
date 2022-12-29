class Solution:
    def freqAlphabets(self, s: str) -> str:
        length = len(s)
        mapped = []
        index = 0
        while index < length:
            if index+2 < length and s[index+2]=='#':
                a = chr(int(s[index] + s[index+1])+96)
                print(a)
                mapped.append(a)
                index += 3
            else:
                a = chr(int(s[index])+96)
                mapped.append(a)
                index += 1
        return "".join(mapped)
