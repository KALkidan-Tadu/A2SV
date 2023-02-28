class Solution:
    k = 1
    def isPowerOfFour(self, n: int) -> bool:
        if self.k==n:
            return True
        if self.k > n:
            return False
        self.k *= 4
        return self.isPowerOfFour(n)
        
