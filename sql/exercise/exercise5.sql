USE myemployees;

SELECT 
    job_id, MAX(salary), MIN(salary), AVG(salary), SUM(salary)
FROM
    employees
GROUP BY job_id
ORDER BY job_id;

SELECT 
    MAX(salary) - MIN(salary) DIFFERENCE
FROM
    employees;

SELECT 
    MIN(salary), manager_id
FROM
    employees
WHERE
    manager_id IS NOT NULL
GROUP BY manager_id
HAVING MIN(salary) >= 6000;

SELECT 
    department_id, COUNT(*), AVG(salary)
FROM
    employees
GROUP BY department_id
ORDER BY AVG(salary) DESC;

SELECT 
    COUNT(*), job_id
FROM
    employees
GROUP BY job_id;
