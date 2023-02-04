class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))
        
        while left <= right:
            product = left*left + right*right
            if product == c:
                return True
            elif product > c:
                right -=1
            else:
                left += 1

        return False
