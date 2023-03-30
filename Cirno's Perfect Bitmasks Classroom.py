testCases = int(input())

for test in range(testCases):
    num = int(input())
    i, j = 0, 0
    n = 0 + num
    m = 0 + num
    while n % 2 == 0 :
        n = n >> 1
        i += 1
    ans = pow(2, i)
    if ans ^ num >0 and num & ans > 0:
        print(ans)
    else:
        while m % 2 == 1 :
            m = m >> 1
            j += 1
    
        print(ans + pow(2, j))
 
