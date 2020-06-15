use myemployees;

SELECT MAX(salary) 最大值,MIN(salary) 最小值,AVG(salary) 平均值,SUM(salary) 和
FROM employees;

SELECT 
    DATEDIFF(MAX(hiredate), MIN(hiredate)) DIFFERENCE
FROM
    employees;

SELECT DATEDIFF('1995-2-7','1995-2-1');

SELECT 
    COUNT(*), department_id
FROM
    employees
WHERE
    department_id = 90;