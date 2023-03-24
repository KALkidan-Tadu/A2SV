class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        index = 0
        n = len(nums)
        while index < n:
            correct = nums[index] - 1
            if nums[index] != nums[correct]:
                nums[index], nums[correct] = nums[correct], nums[index]
            else:
                index += 1

        for i in range(n):
            if nums[i] != i+1:
                return nums[i]
