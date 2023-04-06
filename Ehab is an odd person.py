n = int(input())
nums = list(map(int, input().split()))

odd = False
even = False

for num in nums:
    if num % 2 == 0:
        even = True
    else:
        odd = True

if odd and even:
    nums.sort()
print(*nums)
