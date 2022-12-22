def pileUp(size):
    blocks = [int(item) for item in input().split()]
    left=0
    right=len(blocks)-1
    cube = max(blocks[right], blocks[left])
    yes = True
    while left<=right:
        if (blocks[left]>cube or blocks[right]>cube):
            yes=False
            break
        elif (blocks[right]>=blocks[left]):
            cube = blocks[right]
            right-=1
        else:
            cube = blocks[left]
            left+=1
    if yes:
        print("Yes")
    else:
        print("No")
test_case = int(input())
for i in range(test_case):
    n = int(input())
    pileUp(n)
