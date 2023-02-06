class Solution:
    def reverse(self, arr, index):
        left = 0
        right = index
        while(left <= right):
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    def pancakeSort(self, arr: List[int]) -> List[int]:
        indices = []

        for value in range(len(arr), 0, -1):
            for index in range(0, value):
                if arr[index] == value and index == value-1:
                    break
                elif arr[index]==value and index == 0:
                    self.reverse(arr, value-1)
                    indices.append(value)
                elif arr[index]==value:
                    self.reverse(arr, index)
                    self.reverse(arr, value-1)
                    indices.append(index+1)
                    indices.append(value)
        
        return indices
        
