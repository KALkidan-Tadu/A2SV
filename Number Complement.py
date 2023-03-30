class Solution:
    def findComplement(self, num: int) -> int:
        val = len(bin(num)[2:])
        n = pow(2, val) - 1
        return num ^ n
