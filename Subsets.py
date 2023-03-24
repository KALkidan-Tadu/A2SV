class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = [[]]

        def backTrack(arr, index):
            if index >= len(nums):
                return 
            
            for i in range(index, len(nums)):
                arr.append(nums[i])
                answer.append(arr.copy())
                backTrack(arr, i+1)
                arr.pop()
            
        backTrack([], 0)
        return answer
