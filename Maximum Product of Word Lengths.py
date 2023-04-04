class Solution:
    def maxProduct(self, words: List[str]) -> int:
        d = defaultdict(list)
        maxLen = 0
        for index in range(len(words)):
            s = [0]*(26)
            for c in words[index]:
                s[ord(c) - 97] = 1
            val = 0
            for i in range(1, 27):
                if s[i-1] == 1:
                    val += (pow(2, 26 - i))
            d[index] = val
        for i in range(len(words) - 1):
            for j in range(i+1, len(words)):
                if d[i] & d[j] == 0:
                    maxLen = max(maxLen, (len(words[i])*len(words[j])))
        
        return maxLen
            
        
