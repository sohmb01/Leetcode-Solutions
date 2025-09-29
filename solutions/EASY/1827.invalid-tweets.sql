-- Problem ID: 1827
-- Title: Invalid Tweets
-- Runtime: 1683 ms

# Write your MySQL query statement below
select tweet_id from Tweets
where char_length(content) >15;