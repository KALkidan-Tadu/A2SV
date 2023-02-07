class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        arr = []+nums

        for num in nums:
            num = str(num)
            num = num.strip('0')
            arr.append(int(num[::-1]))
           
        return len(set(arr))
        
