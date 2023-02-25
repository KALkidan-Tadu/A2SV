class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        windowSum = sum(nums[:k])
        maxSum = windowSum
        for index in range(n-k):
            windowSum = windowSum - nums[index] + nums[index+k]
            maxSum = max(windowSum, maxSum)
        return maxSum/k
