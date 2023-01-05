class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        rearranged = []
        negative = 0
        positive = 0
        size = int(len(nums)/2)
        for iter in range(size):
            while(nums[negative] > 0):
                negative += 1
            while(nums[positive] < 0):
                positive += 1
            rearranged.append(nums[positive])
            rearranged.append(nums[negative])
            negative += 1
            positive += 1
        return rearranged
