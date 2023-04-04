class Solution:
    def minSteps(self, n: int) -> int:
        sum_ = 0
        d = 2
        while d*d <= n:
            while n % d == 0:
                sum_ += d
                n //= d 
            d += 1
        if n > 1:
            sum_ += n
        return sum_

