class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        indices = []
        for index in range(len(nums)):
            indices.append([nums[index], index])

        def merge(left, right):
            p1 = 0
            p2 = 0
            while p1 < len(left) and p2 < len(right):
                if left[p1][0] > right[p2][0]:
                    p2 += 1
                else:
                    ans[left[p1][1]] += p2 
                    p1 += 1     
            while p1 < len(left):
                ans[left[p1][1]] += p2 
                p1 += 1    
            left.append([inf, len(left)])
            right.append([inf, len(left)])
            i, j = 0, 0
            merged = []
            while i < len(left)-1 or j < len(right)-1:
                if left[i][0] <= right[j][0]:
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
        
        mergeSort(indices)
        return ans
