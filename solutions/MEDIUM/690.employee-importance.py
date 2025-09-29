# Problem ID: 690
# Title: Employee Importance
# Runtime: 135 ms

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
        mp = defaultdict(tuple)
        for employee in employees:
            i, imp, sub = employee.id,employee.importance,employee.subordinates
            mp[i] = (imp,sub)
        res = 0
        q = [id]
        while q:
            i = q.pop()
            res += mp[i][0]
            for s in mp[i][1]:
                q.append(s)
        return res


