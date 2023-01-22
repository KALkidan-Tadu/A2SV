class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)
        maximum = arr[length-1]
        arr[length-1] = -1

        for index in range(length-2, -1, -1):
            temp = arr[index]
            arr[index] = maximum
            maximum = max(maximum, temp)
        
        return arr
