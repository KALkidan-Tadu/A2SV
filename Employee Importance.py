"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        imp = 0

        def dfs(i):
            nonlocal imp
            
            for emp in employees:
                if emp.id == i:
                    imp += emp.importance
                    for sub in emp.subordinates:
                        dfs(sub)
        dfs(id)
        
        return imp
