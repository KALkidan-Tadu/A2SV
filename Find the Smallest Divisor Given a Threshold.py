class Solution:
    def summation(self, nums, mid):
        total = 0
        for num in nums:
            total += ceil(num/mid)
        return total
        
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        while left < right:
            mid = left+(right-left)//2
            d = self.summation(nums, mid)
            if d <= threshold:
                right = mid
            else:
                left = mid + 1
        
        return left


