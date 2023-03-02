class Solution:
    def myPow(self, x: float, n: int) -> float:
        answer = 1
        p = abs(n)

        if p==0:
            return 1
        if p==1:
            answer *= x
        else:
            if p % 2 == 0:
                temp = self.myPow(x, p/2)
                answer = temp * temp
            else:
                temp = self.myPow(x, p-1)
                answer = x*temp
        
        if n < 0:
            return 1/answer
        return answer
        
