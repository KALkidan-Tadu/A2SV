class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum = 0
        minlen = len(nums)+1

        for right in range(len(nums)):
            sum += nums[right]

            while sum >= target:
                minlen = min(minlen, right-left+1)
                sum -= nums[left]
                left += 1
        
        if minlen == len(nums)+1:
            return 0
        return minlen
