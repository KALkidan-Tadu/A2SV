class Solution:
    def findGCD(self, a, b):
        if b == 0:
            return a
        return self.findGCD(b, a%b)
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            gcd = nums[i]
            for j in range(i, len(nums)):
                gcd = self.findGCD(gcd, nums[j])
                if gcd == k:
                    count += 1
        
        return count
