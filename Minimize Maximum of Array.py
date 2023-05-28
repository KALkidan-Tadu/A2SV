class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        answer = 0
        sum_ = 0
        for i in range(len(nums)):
            sum_ += nums[i]
            answer = max(answer, (sum_+i)//(i+1))
        
        return answer

        
        
