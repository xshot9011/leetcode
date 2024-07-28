-- Write your PostgreSQL query statement below
-- https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT Sub.name AS "Employee"
FROM Employee Sub
JOIN Employee Sup ON Sub.managerId = Sup.id
WHERE Sub.salary > Sup.salary
