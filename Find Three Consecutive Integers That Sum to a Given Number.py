class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        numbers = []
        
        if num%3 == 0:
            firstNum = num//3
            numbers.append(firstNum - 1)
            numbers.append(firstNum)
            numbers.append(firstNum + 1)

        return numbers
