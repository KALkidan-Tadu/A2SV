from collections import Counter
testCases = int(input())

for i in range(testCases):
    planets = input().split()
    cost = int(planets[1])
    totalCost = 0
    myList = list(map(int, input().split()))
    myDict = Counter(myList)
    
    for k in myDict.keys():
        totalCost += (min(myDict[k], cost))
        
    print(totalCost)
