class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if(k==len(nums)):
            return
        k = k%len(nums)
        temp = []
        index = len(nums)-k

        for i in range(index, len(nums)):
            temp.append(nums[i])
        
        for i in range(index):
            temp.append(nums[i])
        
        for i in range(len(temp)):
            nums[i] = temp[i]
        
