class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        count = 0
        score = 0

        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            else:
                count -= 1
                if s[i-1]=="(":
                    score += pow(2, count)
                    
        return score

        
