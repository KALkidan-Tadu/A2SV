n = int(input())
array = []

for i in range(n):
    row = list(map(int, input().split()))
    array.append(row)
source = []
sink = []

for col in range(len(array[0])):
    sum_ = 0
    for row in range(len(array)):
        sum_ += array[row][col]
    if sum_ == 0:
        source.append(col+1)
for row in range(len(array)):
    sum_ = 0
    for col in range(len(array[0])):
        sum_ += array[row][col]
    if sum_ == 0:
        sink.append(row+1)
print(len(source), end = " ")
print(*source)
print(len(sink), end = " ")
print(*sink)
