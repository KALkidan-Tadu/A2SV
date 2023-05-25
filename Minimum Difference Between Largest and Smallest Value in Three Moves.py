class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0
        nums.sort()
        num1 = nums[-1] - nums[3]
        num2 = nums[-4] - nums[0]
        num3 = nums[-3] - nums[1]
        num4 = nums[-2] - nums[2]
        return min(num1, num2, num3, num4) 

