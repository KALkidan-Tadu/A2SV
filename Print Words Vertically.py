class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        vertical = []
        maxlen = len(words[0])
        for i in range(1, len(words)):
            maxlen = max(len(words[i]), maxlen)

        for i in range(maxlen):
            letters = []
            for j in range(len(words)):
                if i<len(words[j]):
                    letters.append(words[j][i])
                else:
                    letters.append(" ")
            vertical.append("".join(letters).rstrip())
        
        return vertical
