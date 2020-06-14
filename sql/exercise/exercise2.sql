use myemployees;
# 1. 查询工资大于 12000 的员工姓名和工资
SELECT 
    first_name, last_name, salary
FROM
    employees
WHERE
    salary >= 12000;

# 查询员工号为 176 的员工的姓名和部门号和年薪

SELECT 
    first_name, last_name, department_id, salary
FROM
    employees
WHERE
     employee_id = 176;
     
# 选择工资不在 5000 到 12000 的员工的姓名和工资
SELECT 
    first_name, last_name, salary
FROM
    employees
WHERE
    salary < 5000 OR salary > 12000;
    
# 选择在 20 或 50 号部门工作的员工姓名和部门号
SELECT 
    first_name, last_name, department_id
FROM
    employees
WHERE
    department_id in(20, 50);
    
# 选择公司中没有管理者的员工姓名及 job_id
SELECT 
    first_name, last_name, salary, commission_pct
FROM
    employees
WHERE
    isnull(manager_id);

SELECT 
    first_name, last_name, salary, commission_pct
FROM
    employees
WHERE
    manager_id is null;
# 选择公司中有奖金的员工姓名，工资和奖金级别
SELECT 
    first_name, last_name, salary, commission_pct
FROM
    employees
WHERE
    commission_pct is not null;

# 选择员工姓名的第三个字母是 a 的员工姓名
SELECT 
    first_name, last_name
FROM
    employees
WHERE
    first_name LIKE '__a%';
    
# 显示出表 employees 表中 first_name 以 'e'结尾的员工信息
SELECT 
    *
FROM
    employees
WHERE
    first_name LIKE '%e';

# 显示出表 employees 部门编号在 80-100 之间 的姓名、职位
SELECT 
    first_name, last_name, employee_id
FROM
    employees
WHERE
    department_id between 80 and 100;
    
# 显示出表 employees 的 manager_id 是 100,101,110 的员工姓名、职位
SELECT 
    first_name, last_name, employee_id
FROM
    employees
WHERE
    manager_id in(100, 101, 110);