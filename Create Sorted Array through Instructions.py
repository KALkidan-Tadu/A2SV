class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        nums = []
        cost = 0
        mod = pow(10, 9)+7
        for i in instructions:
            count1 = len(nums) - (bisect_right(nums, i))
            count2 = bisect_right(nums, i-1)
            insort(nums, i)
            cost += min(count1, count2)
            
        return cost % mod 
