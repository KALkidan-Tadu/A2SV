class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indices = defaultdict(int)
        for i in range(len(nums)): 
            indices[nums[i]] = i
        
        for op in operations:
            index = indices[op[0]] 
            nums[index] = op[1]
            indices[op[1]] = index
        
        return nums
