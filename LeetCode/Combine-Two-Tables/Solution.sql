1# Write your MySQL query statement below
2
3SELECT 
4    p.firstName, 
5    p.lastName, 
6    a.city, 
7    a.state
8FROM Person p
9LEFT JOIN Address a 
10    ON p.personId = a.personId;