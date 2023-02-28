class Solution:
    index = 0
    def reverseString(self, s: List[str]) -> None:
        if self.index == len(s)//2:
            return 
        s[self.index], s[len(s)-self.index-1] = s[len(s)-self.index-1], s[self.index]
        self.index += 1

        return self.reverseString(s)
        
