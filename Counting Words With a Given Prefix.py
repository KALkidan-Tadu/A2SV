class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        n = len(pref)
        for word in words:
            point1, point2 = 0, 0
            m = len(word)
            while point1 < n and point2 < m:
                if pref[point1] == word[point2]:
                    point1 += 1
                    point2 += 1
                else:
                    break
            if point1 == n:
                count += 1
        
        return count
