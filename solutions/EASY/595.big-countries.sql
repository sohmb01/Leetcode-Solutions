-- Problem ID: 595
-- Title: Big Countries
-- Runtime: 606 ms

# Write your MySQL query statement below
select name, population, area from World
where area >= 3000000 or population >= 25000000;