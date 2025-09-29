-- Problem ID: 1724
-- Title: Customer Who Visited but Did Not Make Any Transactions
-- Runtime: 2447 ms

# Write your MySQL query statement below
select v.customer_id, count(v.customer_id) AS count_no_trans 
from Visits v left join Transactions t on v.visit_id = t.visit_id
where t.transaction_id is null 
group by v.customer_id;