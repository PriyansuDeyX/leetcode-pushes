1# Write your MySQL query statement below
2SELECT 
3    e.name AS Employee
4FROM 
5    Employee e,
6    Employee m
7WHERE 
8    e.managerId = m.id
9    AND e.salary > m.salary;