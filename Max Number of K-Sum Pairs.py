class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        oper = 0
        diff = defaultdict(int)

        for num in nums:
            if diff[k-num] > 0:
                oper += 1
                diff[k-num] -= 1
            else:
                diff[num] += 1
        
        return oper
