class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        nums1 = list(map(int, num1[:-1].split('+')))
        nums2 = list(map(int, num2[:-1].split('+')))

        return str(nums1[0]*nums2[0] - nums2[1]*nums1[1]) + "+" + str(nums1[0]*nums2[1] + nums1[1]*nums2[0])+"i"
