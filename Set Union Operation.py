size1 = int(input())
firstSet = set(map(int, input().split()))
size2 = int(input())
secondSet = set(map(int, input().split()))
unionSet = firstSet.union(secondSet)
print(len(unionSet))
