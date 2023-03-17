class Solution:
    def contains(self, big, small):
        return all(big[k] >= small[k] for k in small)

    def minWindow(self, s: str, t: str) -> str:
        count_t = Counter(t)
        left = 0
        count_s = defaultdict(int)
        minLen = len(s)+1
        start, end = -1, -1

        for right in range(len(s)):
            count_s[s[right]] += 1
            while self.contains(count_s, count_t):
                if right - left + 1 < minLen:
                    start = left
                    end = right
                    minLen = right - left + 1

                count_s[s[left]] -= 1
                left += 1
        
        if minLen == len(s)+1:
            return ""
        return s[start: end+1]
