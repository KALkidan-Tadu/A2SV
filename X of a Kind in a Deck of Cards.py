class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        d = Counter(deck)
        arr = []
        for k in d.keys():
            arr.append(d[k])
        print(arr)
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        ans = arr[0] 
        for i in range(1, len(arr)):
            ans = gcd(ans, arr[i])
        if ans > 1:
            return True
        return False
