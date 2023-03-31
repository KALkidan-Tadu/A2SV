class Solution:
    def gcd(a, b):
        if b == 0:
            return a
        return gcd(b, b%a) 
    def findGCD(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)

        return gcd(maximum, minimum)
