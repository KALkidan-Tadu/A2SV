class Solution:
    def sortColors(self, nums: List[int]) -> None:
        red, white, blue = 0, 0, 0
        index = 0

        for num in nums:
            if num == 0:
                red += 1
            elif num == 1:
                white += 1
            else:
                blue += 1
        
        for i in range(red):
            nums[index] = 0
            index += 1
        for i in range(white):
            nums[index] = 1
            index += 1
        for i in range(blue):
            nums[index] = 2
            index += 1
