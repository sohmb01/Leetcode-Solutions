-- Problem ID: 620
-- Title: Not Boring Movies
-- Runtime: 219 ms

# Write your MySQL query statement below

select * from Cinema 
where id%2 = 1 and description != "boring"
order by rating desc;