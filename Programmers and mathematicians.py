testCases = int(input())

for iterations in range(testCases):
    prog, mat = map(int, input().split())
    
    print(min((prog+mat)//4, prog, mat))
