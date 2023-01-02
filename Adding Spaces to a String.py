class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = []
        index = 0
        for i in range(len(s)):
            if index >= len(spaces) or (index<len(spaces) and i<spaces[index]):
                answer.append(s[i])
            elif index<len(spaces) and i==spaces[index]:
                answer.append(" ")
                answer.append(s[i])
                index += 1
        return("".join(answer))
