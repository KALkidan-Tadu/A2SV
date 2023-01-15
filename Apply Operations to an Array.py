class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(1, len(nums)):
            if nums[index] == nums[index-1]:
                nums[index-1] *= 2
                nums[index] = 0
        
        zero = 0
        nonZ = 0
        while nonZ<len(nums):
            if nums[nonZ] != 0:
                nums[nonZ], nums[zero] = nums[zero], nums[nonZ]
                zero += 1
            nonZ += 1
        return nums
