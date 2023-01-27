class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)

        for index in range(len(nums)):
            nums[index] = arr.index(nums[index])
        
        return nums
