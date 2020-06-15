SELECT NOW();

SELECT 
    employee_id,
    first_name,
    last_name,
    salary,
    salary * 1.2 'new_salary'
FROM
    employees;

SELECT 
    LENGTH(last_name) 长度,
    SUBSTR(last_name, 1, 1) 首字母,
    last_name
FROM
    employees
ORDER BY 首字母;

SELECT 
    CONCAT(last_name,
            ' earns ',
            salary,
            ' monthly but wants ',
            salary * 3)
FROM
    employees
WHERE
    salary = 24000;

SELECT 
    last_name,
    job_id AS job,
    CASE job_id
        WHEN 'AD_PRES' THEN 'A'
        WHEN 'ST_MAN' THEN 'B'
        WHEN 'IT_PROG' THEN 'C'
        WHEN 'SA_PRE' THEN 'D'
        WHEN 'ST_CLERK' THEN 'E'
    END AS Grade
FROM
    employees
WHERE
    job_id = 'AD_PRES';