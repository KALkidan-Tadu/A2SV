class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        left = max(weights)
        right = total

        while left < right:
            mid = left + (right - left)//2
            totalDay = 1
            totalweight = 0
            for weight in weights:
                if totalweight + weight > mid:
                    totalDay += 1
                    totalweight = 0
                totalweight += weight
            if totalDay > days:
                left = mid + 1
            else:
                right = mid

        return right

