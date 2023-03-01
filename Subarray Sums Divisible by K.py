class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainders = defaultdict(int)
        sum = 0
        subarray = 0

        for num in nums:
            sum += num
            if sum % k == 0:
                subarray += 1
            subarray += remainders[sum % k]
            remainders[sum % k] += 1
        
        return subarray

            
            
