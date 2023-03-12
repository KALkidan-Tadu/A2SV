class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1
        right = piles[-1]
        
        while left < right:
            mid = left+(right-left)//2

            total = 0
            for p in piles:
                total += ceil(p/mid)
            if total <= h:
                right = mid
            else:
                left = mid + 1
        
        return right
            
