def main():
    def merge(left, right):
            nonlocal swaps
            
            check = False
            if left[0] > right[0]:
                check = True
                swaps += 1
            merged = []
            if check:
                for i in right:
                    merged.append(i)
                for j in left:
                    merged.append(j)
            else:
                for i in left:
                    merged.append(i)
                for j in right:
                    merged.append(j)
            return merged
            
    def mergeSort(arr):
        if len(arr) == 1:
            return arr
        
        mid = len(arr)//2
        left = mergeSort(arr[:mid])
        right = mergeSort(arr[mid:])
        
        return merge(left, right)
    testCase = int(input())
    
    for test in range(testCase):
        n = int(input())
        nums = list(map(int, input().split()))
        swaps = 0
        nums = mergeSort(nums)
        correct = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                correct = False
                break
        if correct:
            print(swaps)
        else:
            print(-1)
main()
