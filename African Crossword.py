n, m = map(int, input().split())
cross = []
check = []
for i in range(n):
    c = [1] * m
    africa = []
    word = input()
    for letter in word:
        africa.append(letter)
    cross.append(africa)
    check.append(c)

for row in range(n):
    for col in range(m):
        curr = cross[row][col]
        found = False
        c = col + 1
        while c < m:
            if cross[row][c] == curr:
                check[row][c] = 0
                found = True
            c += 1
        r = row + 1
        while r < n:
            if cross[r][col] == curr:
                check[r][col] = 0
                found = True
            r += 1
        if found:
            check[row][col] = 0

answer = []
for row in range(n):
    for col in range(m):
        if check[row][col] == 1:
            answer.append(cross[row][col])
print("".join(answer))
