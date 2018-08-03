SELECT Name AS Customers
FROM Customers as c
LEFT JOIN Orders as o ON c.Id = o.CustomerId
WHERE o.CustomerId IS NULL
