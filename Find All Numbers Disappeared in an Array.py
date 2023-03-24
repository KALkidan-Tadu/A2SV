class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missing = []
        n = len(nums)
        index = 0
        while index < n:
            correct = nums[index] - 1
            if nums[index] != nums[correct]:
                nums[index], nums[correct] = nums[correct], nums[index]
            else:
                index += 1
        
        for i in range(len(nums)):
            if nums[i] != i+1:
                missing.append(i+1)
        
        return missing
        
