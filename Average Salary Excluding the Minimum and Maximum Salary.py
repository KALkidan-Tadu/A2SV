class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        sum = 0
        for i in range(len(salary)-1):
            if i==0:
                continue
            else:
                sum += salary[i]
        return(sum/(len(salary)-2))
