class Solution:
    def similarPairs(self, words: List[str]) -> int:
        answer = 0
        myList = list(map(set, words))
        for i in range(len(myList)):
            for j in range(i+1, len(myList)):
                if myList[i] == myList[j]:
                    answer += 1
        return answer
