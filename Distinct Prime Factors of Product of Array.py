class Solution:
    def findPrime(self, product):
        d = 2
        fact = []
        while d*d <= product:
            while product % d == 0:
                fact.append(d)
                product //= d
            d += 1
        if product > 1:
            fact.append(product)
        return set(fact)
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        allSet = set()
        for num in nums:
            s = self.findPrime(num)
            allSet = allSet.union(s)
        
        return len(allSet)
