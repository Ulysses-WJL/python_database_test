USE myemployees;

SELECT 
    last_name, job_id, salary AS sal
FROM
    employees;
    
select * from employees;

select employee_id , last_name,
	salary * 12 AS "ANNUAL SALARY"
from employees;

# 显示表 departments 的结构，并查询其中的全部数据

DESC departments;
SELECT * FROM departments;	

# 显示出表 employees 中的全部 job_id（不能重

SELECT DISTINCT
    job_id
FROM
    employees; 
    
# 显示出表 employees 的全部列，各个列之间用逗号连接，列头显示成 OUT_PUT
SELECT 
    CONCAT(employee_id,
            ',',
            first_name,
            ',',
            email,
            ',',
            IFNULL(commission_pct, 0)) AS OUT_PUT
FROM
    employees;