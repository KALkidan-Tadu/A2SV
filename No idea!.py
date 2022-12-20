n,m = [int(x) for x in input().split()]
A = (int(x) for x in input().split())
B = (int(x) for x in input().split())
c = (int(x) for x in input().split())
B = set(B)
c = set(c)
happy = 0
for i in A:
    if i in B:
        happy += 1
    elif i in c:
        happy -= 1
print(happy)
