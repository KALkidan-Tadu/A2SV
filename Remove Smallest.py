testCases = int(input())

for iterations in range(testCases):
    size = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    
    right = True
    
    for index in range(1, size):
        if nums[index] - nums[index-1] > 1:
            right = False
            break
    
    if right:
        print("YES")
    else:
        print("NO")
