class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = n+m-1
        cur1 = m-1
        cur2 = n-1
        while end >= 0:
            if (cur1>=0 and cur2>=0 and nums1[cur1] >= nums2[cur2]):
                nums1[end] = nums1[cur1] 
                cur1 -= 1
            elif (cur1>=0 and cur2>=0) or (cur2>=0):
                nums1[end] = nums2[cur2]
                cur2 -= 1
            else:
                nums1[end] = nums1[cur1]
                cur1-=1
            end -= 1
