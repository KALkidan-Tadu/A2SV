class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        val = [0] * (n+1) 
        val[1] = 1
        def calculate(n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            if val[n] == 0:
                if n % 2 == 0:
                    val[n] = calculate(n//2)
                else:
                    val[n] = calculate(n//2) + calculate((n//2)+1)
            return val[n]

        for i in range(2, n+1):
            calculate(i)
        return max(val)   
                    
        
