class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxfreq = 0
        left = 0
        characters = defaultdict(int)

        for right in range(len(s)):
            characters[s[right]] += 1
            maxfreq = max(maxfreq, characters[s[right]])
            if right-left+1 > maxfreq+k:
                characters[s[left]] -= 1
                left += 1
            
        if maxfreq+k > len(s):
            return len(s)
        return maxfreq+k



    
