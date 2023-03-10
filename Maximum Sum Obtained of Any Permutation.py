class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        mod = pow(10, 9) + 7
        freq = [0 for _ in range(n)]
        for index in range(len(requests)):
            freq[requests[index][0]] += 1
            if requests[index][1] < n-1:
                freq[requests[index][1]+1] -= 1
        
        for i in range(1, n):
            freq[i] += freq[i-1]
        
        freq.sort()
        nums.sort()
        totalSum = 0
        for index in range(n-1, -1, -1):
            totalSum += (freq[index]* nums[index])
        
        return int(totalSum % mod)


