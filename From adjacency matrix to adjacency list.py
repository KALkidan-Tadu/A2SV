n = int(input())
arr = []

for i in range(n):
    rows = list(map(int, input().split()))
    arr.append(rows)
    
for row in range(len(arr)):
    ans = []
    for col in range(len(arr[row])):
        if arr[row][col] == 1:
            ans.append(col + 1)
    print(len(ans), end = " ")
    print(*ans)
