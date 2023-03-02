class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mono = []
        greater = [-1]*len(nums)

        for i in range(2*len(nums)):
            p = i%len(nums)
            while len(mono) != 0 and nums[mono[len(mono)-1]] < nums[p]:
                index = mono.pop()
                greater[index] = nums[p]
            
            mono.append(p)
        
        return greater
        
