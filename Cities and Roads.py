n = int(input())
arr = []
roads = 0

for i in range(n):
    rows = list(map(int, input().split()))
    arr.append(rows)
    
for row in range(len(arr)):
    for col in range(row, len(arr)):
        if arr[row][col] == 1:
            roads += 1
print(roads)
