from collections import Counter
k = int(input())

myList = list(map(int, input().split()))
myDict = Counter(myList)

for key in myDict.keys():
    if myDict[key] != k:
        print(key)
