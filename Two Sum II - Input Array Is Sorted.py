class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        nums = {}
        indices = []

        for index in range(len(numbers)):
            diff = target-numbers[index]
            if diff in nums:
                index1 = nums[diff]
                return [index1+1, index+1]
            nums[numbers[index]] = index  

