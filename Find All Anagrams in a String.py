class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        count_p = Counter(p)
        window = Counter(s[:n-1])
        indices = []

        for index in range(n-1, len(s)):
            window[s[index]] += 1
            if count_p == window:
                indices.append(index-n+1)
            window[s[index-n+1]] -= 1

        return indices
     

        

