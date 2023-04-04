class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for i in range(32):
            count = 0
            val = 1 << i
            for num in nums:
                if num & val != 0:
                    count += 1
            if count % 3 != 0:
                answer += 0 ^ val
        if answer > pow(2, 31) - 1:
            return answer - pow(2, 32)
        return answer
