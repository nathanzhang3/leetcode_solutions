# Write your MySQL query statement below
SELECT e.Name AS Employee
    FROM Employee AS e,
         Employee AS m
    WHERE e.ManagerId = m.Id
    AND e.Salary > m.Salary