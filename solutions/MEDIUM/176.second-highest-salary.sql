-- Problem ID: 176
-- Title: Second Highest Salary
-- Runtime: 180 ms

# Write your MySQL query statement 
select max(Salary) as SecondHighestSalary from Employee where Salary<(select max(Salary) from Employee) ;