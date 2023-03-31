class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n%2 == 0:
            index = 1
        else:
            index = 0
        num = 0 
        size = len(bin(n)[2:])
        while index <= size:
            num += pow(2, index)
            index += 2
        return (num ^ n == 0)
