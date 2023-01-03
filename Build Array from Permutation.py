class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        permutation = []
        for index in range(len(nums)):
            permutation.append(nums[nums[index]])
        
        return permutation
