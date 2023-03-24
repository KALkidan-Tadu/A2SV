class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        repeated = []
        index = 0

        while index < n:
            correct = nums[index] - 1
            if nums[index] != nums[correct]:
                nums[index], nums[correct] = nums[correct], nums[index]
            else:
                index += 1
        
        for i in range(n):
            if nums[i] != i+1:
                repeated.append(nums[i])
        
        return repeated
