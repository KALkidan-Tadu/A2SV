class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        diff = defaultdict(int)
        diff[0] = 1
        sum = 0
        subarray = 0

        for num in nums:
            sum += num
            subarray += diff[sum-goal]
            diff[sum] += 1
        
        return subarray
