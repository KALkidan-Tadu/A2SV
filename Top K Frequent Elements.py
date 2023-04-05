class Solution:
    def quickSort(self, nums, left, right):
        if left >= right:
            return
        pivot = left
        read = pivot + 1
        write = pivot + 1

        while read <= right:
            if nums[pivot][0] >= nums[read][0]:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            read += 1

        nums[pivot], nums[write - 1] = nums[write - 1], nums[pivot]
        
        pivot = write - 1

        self.quickSort(nums,pivot+1,right)

        self.quickSort(nums,left,pivot-1)


    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = []
        for key in count.keys():
            arr.append([count[key], key])
        self.quickSort(arr, 0, len(arr)-1)
        frequent = []
        i = 1
        n = len(arr)
        while i <= k:
            frequent.append(arr[n-i][1])
            i += 1
        return frequent

                    
