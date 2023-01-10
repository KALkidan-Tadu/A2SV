class Solution:
    def findNum(self, num):
        numbers = {"0":0, "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
        factor = 1
        number = 0
        for index in range(len(num)-1, -1, -1):
            number += numbers[num[index]] * factor
            factor *= 10
        return number

    def multiply(self, num1: str, num2: str) -> str:
        num1 = self.findNum(num1)
        num2 = self.findNum(num2)
        return str(num1*num2)
