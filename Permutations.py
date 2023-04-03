class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backTrack(arr, left, right):
            if left == right:
                answer.append(arr.copy())
                return 
            
            for i in range(left, right):
                arr[left], arr[i] = arr[i], arr[left]
                backTrack(arr, left+1, right)
                arr[left], arr[i] = arr[i], arr[left]
        arr = []+nums
        backTrack(arr, 0, len(nums))
        return answer
