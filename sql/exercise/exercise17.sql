# 1、创建函数，实现传入两个float，返回二者之和
DELIMITER $
CREATE FUNCTION test_f1(f1 FLOAT, f2 FLOAT) RETURNS FLOAT 
BEGIN
   DECLARE SUM FLOAT DEFAULT 0;
   SET SUM := f1 + f2;
   RETURN SUM;
END $
SELECT test_f1(1.5, 2)$

# 创建函数，实现传入工种名，返回该工种的员工人数

CREATE FUNCTION test_func2(job_name VARCHAR(35)) RETURNS INT
BEGIN
    DECLARE num INT DEFAULT 0;
    SELECT COUNT(*) INTO num
    FROM employees
    WHERE job_id = job_name;
    RETURN num;
END $
SELECT test_func2('AD_PRES')$

# 创建函数，实现传入员工名，返回该员工的领导名
CREATE FUNCTION test_f3(e_name VARCHAR(25)) RETURNS VARCHAR(25)
BEGIN
	DECLARE m_name VARCHAR(25) DEFAULT NULL;
	SELECT m.last_name INTO m_name
	FROM employees m
	JOIN employees e ON e.manager_id = m.employee_id
	WHERE e_name = e.last_name;
	RETURN m_name;
END $

SELECT test_f3('Urman') $
