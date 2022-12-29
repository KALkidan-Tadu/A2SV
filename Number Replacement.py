testCases = int(input())

for i in range(testCases):
    myDict = {}
    length = int(input())
    numbers = input().split()
    word = input()
    correct = True
    
    for j in range(length):
        if numbers[j] in myDict and myDict[numbers[j]] != word[j]:
            correct = False
            break
        elif numbers[j] not in myDict:
            myDict[numbers[j]] = word[j]
    if correct:
        print("YES")
    else:
        print("NO")
