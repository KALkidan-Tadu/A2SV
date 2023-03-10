class Solution:
    def calculate(self, n):
        if n == 1:
            return 1
        return (self.calculate(n-1) * 2 +1)

    def findKthBit(self, n: int, k: int) -> str:
        if k == 1:
            return "0"
        length = self.calculate(n)
        if k <= length//2:
            return self.findKthBit(n-1, k)
        if k == (length//2)+1:
            return "1"
        return str(1 - int(self.findKthBit(n-1,length-k+1)))
        



