class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        for i in range(len(nums1)):
            nums1[i] -= nums2[i]
        total = 0
        def merge(left, right):
            nonlocal total
            p1 = 0
            p2 = 0
            while p1 < len(left) and p2 < len(right):
                if left[p1] <= right[p2] + diff:
                    total += len(right) - p2
                    p1 += 1
                else:
                    p2 += 1
            merged = []
            i, j = 0, 0
            left.append(inf)
            right.append(inf)
            while i < len(left)-1 or j < len(right) - 1:
                if left[i] <= right[j]:
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            return merged
        def mergeSort(arr):
            if len(arr) == 1:
                return arr
            mid = len(arr)//2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])

            return merge(left, right)   
        mergeSort(nums1) 
        return total  
