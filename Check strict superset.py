A = set(input().split())
n = int(input())
b = set()
for i in range (n):
    b = b.union(set(input().split()))
if A.issuperset(b):
    print(True)
else:
    print(False)
