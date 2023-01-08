class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        rearranged = []
        p = 0
        
        for num in nums:
            if num == pivot:
                p += 1
            elif num < pivot:
                rearranged.append(num)

        while p > 0:
            rearranged.append(pivot)
            p -= 1

        for num in nums:
            if num > pivot:
                rearranged.append(num)

        return rearranged
