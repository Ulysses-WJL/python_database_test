use myemployees;

SELECT 
    first_name, last_name, department_id, salary *12 * (1 + IFNULL(commission_pct, 0)) 年薪
FROM
    employees
ORDER BY 年薪 DESC , first_name DESC;

select last_name, salary
from employees
where salary not between 8000 and 17000
order by salary desc;

SELECT 
    *, LENGTH(email)
FROM
    employees
WHERE
    email LIKE '%e%'
ORDER BY LENGTH(email) DESC , department_id ASC;