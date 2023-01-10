class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = pow(10,9) + 7
        meals = defaultdict(int)
        res = 0
        for num in deliciousness:
            power = 1
            for i in range(1, 23):
                if power-num in meals:
                    res += meals[power-num]
                power *= 2
            meals[num] += 1
            
        return res%mod
