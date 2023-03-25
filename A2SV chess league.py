n, k = map(int, input().split())
nums = list(map(int, input().split()))
arr = []
for i in range(1, pow(2,n)+1):
    arr.append(i)

def winner(arr):
    if len(arr) == 1:
        return arr
    
    mid = int(len(arr)/2)
    left = winner(arr[:mid])
    right = winner(arr[mid:len(arr)])
    answer = []
    minL, minR = float("inf"), float("inf")
    
    for i in left:
        minL = min(minL, nums[i - 1])
    for i in right:
        minR = min(minR, nums[i - 1])
    
    for index in left:
        if nums[index - 1] >= minR or abs(nums[index - 1] - minR) <= k:
            answer.append(index)
    
    for index in right:
        if nums[index - 1] >= minL or abs(nums[index - 1] - minL) <= k:
            answer.append(index)
    
    return answer
print(*winner(arr))
