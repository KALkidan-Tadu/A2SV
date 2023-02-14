n,m = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

nums1.sort()
index = 0
indices = []

for num in nums2:
    while index < n and nums1[index] < num:
        index += 1
    indices.append(index)
    
print(*indices)
