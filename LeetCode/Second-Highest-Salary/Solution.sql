1# Write your MySQL query statement below
2SELECT MAX(salary) AS SecondHighestSalary
3FROM Employee
4WHERE salary < (SELECT MAX(salary) FROM Employee);