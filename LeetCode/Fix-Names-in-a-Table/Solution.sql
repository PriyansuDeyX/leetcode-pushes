1# Write your MySQL query statement below
2
3SELECT 
4    user_id,
5    CONCAT(
6        UPPER(SUBSTRING(name, 1, 1)),
7        LOWER(SUBSTRING(name, 2))
8    ) AS name
9FROM Users
10ORDER BY user_id;
11