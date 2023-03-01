class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = -inf

        for index in range(len(nums)-1, -1, -1):
            if nums[index] < k:
                return True
            while len(stack) != 0 and stack[len(stack)-1] < nums[index]:
                k = stack.pop()
            stack.append(nums[index])
        
        return False
             
