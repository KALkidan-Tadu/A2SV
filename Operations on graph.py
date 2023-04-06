from collections import defaultdict
n = int(input())
k = int(input())
d = defaultdict(list)

for i in range(k):
    opr = list(map(int, input().split()))
    if opr[0] == 1:
        d[opr[1]].append(opr[2])
        d[opr[2]].append(opr[1])
    else:
        print(*d[opr[1]])
