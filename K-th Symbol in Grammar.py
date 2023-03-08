class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0
        odd = k % 2
        k = ceil(k/2)
        if odd == 1:
            return self.kthGrammar(n-1, k)
        return 1 - self.kthGrammar(n-1, k)       
