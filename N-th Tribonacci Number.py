class Solution:
    def tribonacci(self, n: int) -> int:
        val = defaultdict(int)
        def calculate(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if not val[n]:
                val[n] = calculate(n-1) + calculate(n-2) + calculate(n-3)
            return val[n]
        return calculate(n)
