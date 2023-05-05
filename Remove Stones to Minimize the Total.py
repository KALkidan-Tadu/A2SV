class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1
        heapify(piles)
        for i in range(k):
            stone = -1 * heappop(piles)
            if stone % 2 == 0:
                stone /= 2
            else:
                stone = 1 + (stone // 2)
            heappush(piles, int(-1 * stone))
        
        return -1 * sum(piles)
