class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primes = [1]*(right + 1)
        primes[0] = 0
        primes[1] = 0

        i = 2
        while i * i <= right +1:
            if primes[i] == 1:
                j = i * i
                while j < right + 1:
                    primes[j] = 0
                    j += i
            i += 1
        nums = []
        for index in range(left, len(primes)):
            if primes[index] == 1:
                nums.append(index)
        res = [-1, -1]
        mindist = right + 1
        for i in range(len(nums)-1, 0, -1):
            if nums[i] - nums[i-1] <= mindist:
                mindist = nums[i]- nums[i-1]
                res[0] = nums[i-1]
                res[1] = nums[i]
        return res
