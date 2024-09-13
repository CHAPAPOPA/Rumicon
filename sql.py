"""SELECT Employees.name,
       Contracts.type,
       Positions.salary,
       (Positions.salary * Contracts.tax_rate / 100) AS tax_amount
FROM Employees
JOIN Positions ON Employees.position_id = Positions.id
JOIN Contracts ON Employees.contract_id = Contracts.id
WHERE Positions.salary < 50000;"""
