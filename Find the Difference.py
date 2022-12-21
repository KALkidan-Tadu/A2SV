class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        from collections import Counter
        d = Counter(s)
        for i in range(len(t)):
            d[t[i]] -= 1
            if d[t[i]] == -1:
                return t[i]
