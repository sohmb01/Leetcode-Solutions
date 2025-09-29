-- Problem ID: 577
-- Title: Employee Bonus
-- Runtime: 1885 ms

# Write your MySQL query statement below

select e.name, b.bonus 
from Employee e left outer join Bonus b on e.empId = b.empId
where b.bonus<1000 or b.bonus is null;