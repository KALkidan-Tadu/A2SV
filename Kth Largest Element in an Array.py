class Solution:
    def quickSort(self, nums, left, right,k):
        if left >= right:
            return nums[left]
        pivot = left
        pivot = left
        read = pivot + 1
        write = pivot + 1

        while read <= right:
            if nums[pivot] >= nums[read]:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            read += 1

        nums[pivot], nums[write - 1] = nums[write - 1], nums[pivot]
        
        pivot = write - 1

        if k == len(nums) - pivot:
            return nums[pivot]
        elif len(nums) - k >pivot:
            return self.quickSort(nums,pivot+1,right,k)

        return self.quickSort(nums,left,pivot-1,k)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSort(nums,0,len(nums)-1, k)
