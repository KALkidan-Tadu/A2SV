class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        w1 = list(word1)
        w2 = list(word2)
        answer = []
        while w1 and w2:
            if w1 >= w2:
                answer.append(w1.pop(0))
            else:
                answer.append(w2.pop(0))
        
        return("".join(answer)+"".join(w1)+"".join(w2))
