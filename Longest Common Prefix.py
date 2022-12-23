class Solution:
    def compare(self, s1, s2):
        s = ""
        i = 0
        while i<len(s1) and i<len(s2):
            if s1[i] == s2[i]:
                s += s1[i]
            else:
                break
            i += 1
        return s


    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        answer = self.compare(strs[0], strs[1])
        if len(strs)==2:
            return answer
        j = 2
        while j<len(strs):
            answer = self.compare(strs[j], answer)
            j += 1
        return answer
