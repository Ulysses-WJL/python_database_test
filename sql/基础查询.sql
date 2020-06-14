# 基础查询
SHOW DATABASES;
USE myemployees;

SELECT first_name FROM employees;
SELECT 
    first_name, last_name
FROM
    employees;
    
SELECT * FROM employees;    

# 查询常量值
SELECT "Valli";

# 查询表达式
SELECT  100%98 AS result;

# 查询函数
SELECT 	VERSION();

# 起别名 as  空格
SELECT first_name AS 姓 , last_name AS 名 FROM employees;
SELECT first_name 姓 , last_name 名 FROM employees;
SELECT salary AS "out put" FROM employees;

# 去重
SELECT DISTINCT department_id FROM employees;

# + 号  : 加法计算
SELECT 100 + 20;  # 120
SELECT '100' + 20;  # 120
SELECT 'aaa' + 100;  # 100

SELECT CONCAT(first_name, ' ', last_name) AS 姓名 FROM employees;

# 显示表结构
DESC employees;

SELECT IFNULL(commission_pct, 0) AS 奖金 FROM employees;