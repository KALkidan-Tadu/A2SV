class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = set()

        def backTrack(arr, index):
            if index == len(nums):
                return 
            
            for i in range(index, len(nums)):
                if len(arr) == 0 or arr[-1] <= nums[i]:
                    arr.append(nums[i])
                    if len(arr) >= 2:
                        answer.add(tuple((arr)))
                    backTrack(arr.copy(), i+1)
                    arr.pop()
            
        backTrack([], 0)
        return list(answer)
