class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = [0] * 3
        for bill in bills:
            if bill == 5:
                money[0] += 1
            elif bill == 10:
                if money[0] == 0:
                    return False
                money[0] -= 1
                money[1] += 1
            else:
                if money[1] == 0 and money[0] <= 2:
                    return False
                if money[1] > 0:
                    if money[0] == 0:
                        return False
                    money[1] -= 1
                    money[0] -= 1
                    money[2] += 1
                else:
                    if money[0] < 3:
                        return False
                    money[0] -= 3
                    money[2] += 1
        return True
                    
