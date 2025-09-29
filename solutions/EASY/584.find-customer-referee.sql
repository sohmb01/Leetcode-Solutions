-- Problem ID: 584
-- Title: Find Customer Referee
-- Runtime: 951 ms

# Write your MySQL query statement below
select name from Customer where referee_id is null or not referee_id = 2 ;