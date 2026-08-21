1# Write your MySQL query statement below
2
3select max(salary) as SecondHighestSalary from Employee where salary not in (select max(salary) from Employee);