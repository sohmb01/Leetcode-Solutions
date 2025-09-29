-- Problem ID: 175
-- Title: Combine Two Tables
-- Runtime: 346 ms

# Write your MySQL query statement below
Select FirstName,LastName,City,State from Person left join Address on Person.PersonId=Address.PersonId;