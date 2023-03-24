class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        minimum = min(nums)
        index = 0
        n = len(nums)

        for index in range(n):
            while nums[index] != index and nums[index] < n:
                correct = nums[index]
                nums[index], nums[correct] = nums[correct], nums[index]

        for i in range(n):
            if nums[i] != i:
                return i
        return n
        
