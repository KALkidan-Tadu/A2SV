class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = defaultdict(int)
        left = 0
        maxlen = 0

        for right in range(len(s)):
            unique[s[right]] += 1
            while unique[s[right]] > 1:
                unique[s[left]] -= 1
                left += 1
            maxlen = max(maxlen, right-left+1)
        
        return maxlen
