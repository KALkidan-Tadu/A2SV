class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        s1_count = Counter(s1)
        window = Counter(s2[:size-1])
        left = 0

        for right in range(size-1, len(s2)):
            window[s2[right]] += 1
            if window == s1_count:
                return True
            window[s2[left]] -= 1
            left += 1
            
        return False
