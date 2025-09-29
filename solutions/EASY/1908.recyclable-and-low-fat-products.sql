-- Problem ID: 1908
-- Title: Recyclable and Low Fat Products
-- Runtime: 2121 ms

# Write your MySQL query statement below
SELECT product_id FROM Products WHERE low_fats = 'Y' AND recyclable='Y';