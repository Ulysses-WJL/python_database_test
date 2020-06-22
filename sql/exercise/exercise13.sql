USE books;
# 创建一个表，里面有id为主键，stuname 唯一键，seat座位号，要求将id设置成自增
CREATE TABLE s1(
  id INT PRIMARY KEY AUTO_INCREMENT,
  studname VARCHAR(20) UNIQUE
);

INSERT INTO s1 VALUES (7, 's5');

# 要求用事务的方式插入3行数据
SET autocommit=0;
START TRANSACTION;
INSERT INTO s1 VALUES (1, 's1'), (2, 's2'), (3, 's3');
COMMIT;

SELECT * FROM s1;

# 要求用事务的方式删除数据，并回滚
SET autocommit=0;
START TRANSACTION;
DELETE FROM s1;
SELECT * FROM s1;

ROLLBACK;
