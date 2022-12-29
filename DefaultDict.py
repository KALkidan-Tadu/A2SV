length = input().split()
n = int(length[0])
m = int(length[1])
A = []
B = []

for i in range(n):
    A.append(input())

for j in range(m):
    B.append(input())

for numB in B:
    if numB not in A:
        print(-1)
    else:
        for index in range(n):
            if A[index] == numB:
                print(index+1, end=" ")
        print()       
