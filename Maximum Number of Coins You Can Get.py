class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        myPart = 0
        piles.sort()
        index = len(piles)-2

        for i in range(len(piles)//3):
            myPart += piles[index]
            index -= 2
        
        return myPart
