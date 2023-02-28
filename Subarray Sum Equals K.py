class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        s = 0
        subarray = 0

        for num in nums:
            s += num
            if s == k:
                subarray += 1
            subarray += sums[s-k]
            sums[s] += 1

        return subarray 

