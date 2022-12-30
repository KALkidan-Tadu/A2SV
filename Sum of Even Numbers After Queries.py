class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sum = 0
        answer = []
        for num in nums:
            if num%2 == 0:
                sum += num
        
        for i in range(len(queries)):
            if nums[queries[i][1]] % 2 == 0:
                sum -= nums[queries[i][1]]
            nums[queries[i][1]] += queries[i][0]
            if nums[queries[i][1]] % 2 == 0:
                sum += nums[queries[i][1]]
            answer.append(sum)
            
        return answer
