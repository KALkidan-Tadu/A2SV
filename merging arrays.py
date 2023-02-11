size1, size2 = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

merged = []
pointer1, pointer2 = 0, 0

while pointer1<size1 and pointer2<size2:
    if nums1[pointer1] <= nums2[pointer2]:
        merged.append(nums1[pointer1])
        pointer1 += 1
    else:
        merged.append(nums2[pointer2])
        pointer2 += 1

while pointer1<size1:
    merged.append(nums1[pointer1])
    pointer1 += 1

while pointer2<size2:
    merged.append(nums2[pointer2])
    pointer2 += 1
    
print(*merged)
