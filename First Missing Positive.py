class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            while nums[index] != index + 1 and nums[index] > 0 and nums[index] < len(nums):
                correct = nums[index] - 1
                if nums[correct] == nums[index]:
                    break
                nums[correct], nums[index] = nums[index], nums[correct]
        
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        
        return len(nums) + 1
