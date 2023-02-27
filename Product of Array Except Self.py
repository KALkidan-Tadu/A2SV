class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        left = [0]*size
        right = [0]*size
        product = []
        left[0] = nums[0]
        right[size-1] = nums[size-1]

        for index in range(1, size):
            left[index] = left[index-1] * nums[index]
        
        for index in range(size-2, -1, -1):
            right[index] = right[index+1] * nums[index]
        
        for index in range(size):
            if index == 0:
                product.append(right[index+1])
            elif index == size-1:
                product.append(left[index-1])
            else:
                product.append(left[index-1] * right[index+1])
        
        return product

