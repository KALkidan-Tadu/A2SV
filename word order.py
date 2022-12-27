from collections import Counter
length = int(input())
myList = []
for i in range(length):
    myList.append(input())
myDict = Counter(myList)
print(len(myDict))
for value in myDict.values():
    print(value, end=" ")

