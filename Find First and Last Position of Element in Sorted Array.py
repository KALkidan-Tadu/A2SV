class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        answer = [bisect_left(nums, target), bisect_right(nums, target)-1]

        if nums[answer[1]] != target:
            return [-1, -1]
        return answer
