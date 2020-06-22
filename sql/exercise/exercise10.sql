USE myemployees;

CREATE TABLE my_employees(
	Id INT(10),
	First_name VARCHAR(10),
	Last_name VARCHAR(10),
	Userid VARCHAR(10),
	Salary DOUBLE(10,2)
);
CREATE TABLE users(
	id INT,
	userid VARCHAR(10),
	department_id INT
);

DESC my_employees;

INSERT INTO my_employees VALUES
(1,'patel', 'Ralph', 'Rpatl', 895),
(2, 'Dancs', 'Betty', 'Bdancs', 860),
(3, 'Biri', 'Ben', 'Bbiri', 1100),
(4, 'Newman', 'Chad', 'Cnewman', 750),
(5, 'Ropeburn', 'Audrey', 'Aropebur', 1550);



INSERT INTO users VALUES
(1, 'Rpatel', 10),
(2, 'Bdancs', 10),
(3, 'Bbiri', 20),
(4, 'Cnewman', 30),
(5, 'Aropebur', 40);

# 将3号员工的last_name修改为“drelxer”

UPDATE my_employees
SET last_name='drelxer' WHERE Id=3;

# 将所有工资少于900的员工的工资修改为1000
UPDATE my_employees
SET Salary=1000 WHERE Salary < 900;

# 将userid 为Bbiri的user表和my_employees表的记录全部删除
DELETE u, e
FROM users u, my_employees e
WHERE u.Userid=e.Userid
AND u.userid = 'Bbiri';

# 删除所有数据
DELETE FROM my_employees;
DELETE FROM users;

# 检查所作的修正
SELECT * FROM my_employees;
SELECT * FROM users;

# 清空表my_employees
TRUNCATE my_employees;
