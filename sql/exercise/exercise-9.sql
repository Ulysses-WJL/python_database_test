USE myemployees;
# 1. 查询和Zlotkey相同部门的员工姓名和工资
SELECT department_id 
FROM employees e
WHERE e.last_name = "Zlotkey";

SELECT first_name, last_name, salary
FROM employees e
WHERE e.department_id = (
	SELECT department_id 
	FROM employees e
	WHERE e.last_name = "Zlotkey"
);

#2.查询工资比公司平均工资高的员工的员工号，姓名和工资。
# 1. 查询公司平均工资
SELECT AVG(salary)
FROM employees;

# 2. 查询salary > 1
SELECT employee_id , first_name, last_name, salary
FROM employees e
WHERE e.salary > (
	SELECT AVG(salary)
	FROM employees
);

#3.查询各部门中工资比本部门平均工资高的员工的员工号, 姓名和工资
# 1.查询各个部门的平均工资
SELECT AVG(salary), department_id
FROM employees
GROUP BY department_id;

# 连接①结果集和employees表，进行筛选
SELECT employee_id, first_name, last_name, salary
FROM employees e
JOIN (
	SELECT AVG(salary) ag, department_id
	FROM employees
	GROUP BY department_id
) avg_
ON e.department_id = avg_.department_id 
WHERE salary > avg_.ag;

#4.查询和姓名中包含字母u的员工在相同部门的员工的员工号和姓名
# 1 查询姓名中包含字母u的员工的部门
SELECT DISTINCT department_id 
FROM employees 
WHERE last_name LIKE '%u%';

# 2. 查询对应部门的员工信息
SELECT last_name, employee_id
FROM employees e
WHERE e.department_id IN(
	SELECT DISTINCT department_id 
	FROM employees 
	WHERE last_name LIKE '%u%'
);

#5. 查询在部门的location_id为1700的部门工作的员工的员工号
# 1 查询在部门的location_id为1700的部门
SELECT DISTINCT department_id
FROM departments
WHERE location_id = 1700;

# 2. 查询对应各部门下员工信息
SELECT employee_id 
FROM employees e
WHERE department_id IN(
	SELECT DISTINCT department_id
	FROM departments
	WHERE location_id = 1700
);


SELECT employee_id
FROM employees
WHERE department_id =ANY(
	SELECT DISTINCT department_id
	FROM departments 
	WHERE location_id  = 1700

);

#6.查询管理者是King的员工姓名和工资
SELECT last_name, salary
FROM employees 
WHERE manager_id IN(
	SELECT employee_id
	FROM employees
	WHERE last_name = "K_ing" 
);

SELECT e.last_name, e.salary
FROM employees e
JOIN employees m ON m.employee_id = e.manager_id
WHERE m.last_name = "K_ing";

#7.查询工资最高的员工的姓名，要求first_name和last_name显示为一列，列名为 
SELECT CONCAT(last_name, first_name) "姓.名"
FROM employees
WHERE salary=(
	SELECT MAX(salary)
	FROM employees
);


