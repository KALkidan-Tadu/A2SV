class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        diff = defaultdict(int)
        diff[0] = 1
        sum = 0
        answer = 0

        for num in nums:
            if num % 2 != 0:
                sum += 1
            answer += diff[sum - k]
            diff[sum] += 1
        
        return answer
            
