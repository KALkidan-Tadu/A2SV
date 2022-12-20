d = {}
n = int(input())
for i in range(n):
    word = input()
    if word in d:
        d[word] += 1
    else:
        d[word] = 1
print(len(d))
for value in d.values():
    print(value, end=" ")
