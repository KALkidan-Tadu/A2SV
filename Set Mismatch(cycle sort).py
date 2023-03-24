class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        index = 0
        n = len(nums)

        while index < n:
            correct = nums[index] - 1
            if nums[correct] != nums[index]:
                nums[correct], nums[index] = nums[index], nums[correct]
            else:
                index += 1
        for i in range(n):
            if nums[i] != i+1:
                return [nums[i], i+1]
