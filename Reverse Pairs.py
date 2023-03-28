class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        total = 0

        def merge(left, right):
            nonlocal total
            p1 = 0
            p2 = 0
            while p1 < len(left) and p2 < len(right):
                if left[p1] > 2 * right[p2]:
                    p2 += 1
                else:
                    total += p2
                    p1 += 1
            while p1 < len(left):
                total += p2
                p1 += 1
            left.append(inf)
            right.append(inf)
            i, j = 0, 0
            merged = []
            while i < len(left)-1 or j < len(right)-1:
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
        mergeSort(nums)
        return total
