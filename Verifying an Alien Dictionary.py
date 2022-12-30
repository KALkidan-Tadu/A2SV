class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        myDict = {}
        for i in range(len(order)):
            myDict[order[i]] = i

        for index in range(len(words)-1):
            for i in range(len(words[index])):
                if i >= len(words[index+1]) :
                    return False
                if words[index][i] != words[index+1][i]:
                    if myDict[words[index][i]] > myDict[words[index+1][i]]:
                        return False
                    break

        return True
