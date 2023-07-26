class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        counter = defaultdict(dict)
        answer = 1

        for i in range(len(nums)):
            for j in range(i):
                val = nums[i] - nums[j]
                if val not in counter[j]:
                    counter[j][val] = 1
                if val not in counter[i]:
                    counter[i][val] = 0
                counter[i][val] = counter[j][val]+1
                answer = max(answer, counter[i][val])               
        
        return answer
