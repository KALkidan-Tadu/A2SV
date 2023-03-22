testCase = int(input())
for test in range(testCase):
    n, m = map(int, input().split())
    nums = []
    for i in range(n):
        num = list(map(int, input().split()))
        nums.append(num)
    maxSum = 0
    for row in range(n):
        for col in range(m):
            r = row - 1
            c = col - 1
            s = nums[row][col]
            while r >=0 and c >= 0:
                s += nums[r][c]
                r -= 1
                c -= 1
            r = row + 1
            c = col + 1
            while r < n and c < m:
                s += nums[r][c]
                r += 1
                c += 1
            r = row - 1
            c = col + 1
            while r >= 0 and c < m:
                s += nums[r][c]
                r -= 1
                c += 1
            r = row + 1
            c = col - 1
            while r < n and c >= 0:
                s += nums[r][c]
                r += 1
                c -= 1
            maxSum = max(maxSum, s)

    print(maxSum)
