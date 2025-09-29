-- Problem ID: 1258
-- Title: Article Views I
-- Runtime: 1920 ms

# Write your MySQL query statement below
select author_id as id from Views 
where author_id = viewer_id 
group by author_id
order by id ;