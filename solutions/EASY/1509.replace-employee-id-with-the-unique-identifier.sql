-- Problem ID: 1509
-- Title: Replace Employee ID With The Unique Identifier
-- Runtime: 2817 ms

# Write your MySQL query statement below
select eu.unique_id , e.name from EmployeeUNI eu right join Employees e on eu.id = e.id;