testCase = int(input())
for test in range(testCase):
    size = int(input())
    nums = list(map(int, input().split()))
    
    left = 0
    right = 0
    maxSum = nums[0]
    sum_ = 0
    
    while right < size:
        if nums[right]*nums[left] < 0:
            sum_ += maxSum
            maxSum = nums[right]
            
        left = right
        maxSum = max(maxSum, nums[right])
        right += 1
    sum_ += maxSum
    print(sum_)
        
        
    
