class Solution:
    def checkTriangle(self, side1, side2, side3):
        if side1+side2> side3 and side2+side3> side1 and side1+side3> side2:
            return True
        else:
            return False
    def largestPerimeter(self, nums: List[int]) -> int:
        maxPerimeter = 0
        nums.sort()
        index = len(nums)-1
        while(index>=2):
            if self.checkTriangle(nums[index], nums[index-1], nums[index-2]):
                maxPerimeter = max(maxPerimeter, nums[index]+nums[index-1]+nums[index-2])
            index -= 1
        return maxPerimeter
