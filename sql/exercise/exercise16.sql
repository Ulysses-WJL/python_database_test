USE girls;
# 创建存储过程或函数实现传入用户名和密码，插入到admin表中
CREATE PROCEDURE pro1(IN username VARCHAR(20), IN passwd VARCHAR(20))
BEGIN
    INSERT INTO admin(admin.username, admin.password)
    VALUES(username, passwd);
END $

SELECT * FROM admin;


# 创建存储过程或函数实现传入女神编号，返回女神名称和女神电话

CREATE PROCEDURE pro2(IN bid INT, OUT bname VARCHAR(50), OUT btel VARCHAR(11))
BEGIN 
    SELECT b.name, b.phone INTO bname, btel
    FROM beauty b
    WHERE bid = b.id;
END $


# 创建存储存储过程或函数实现歘人两个女神生日，返回大小
CREATE PROCEDURE pro3(IN birth1 DATETIME, IN birth2 DATETIME, OUT result INT)
BEGIN
    SELECT DATEDIFF(birth1, birth2) INTO result;
END $

# 创建存储过程或函数实现传入一个日期，格式化成xx年xx月xx日并返回
CREATE PROCEDURE pro4(IN date1 DATETIME, OUT strdate VARCHAR(50))
BEGIN 
	SELECT DATE_FORMAT(date1, '%y年%m月%d日') INTO strdate;
END $


# 创建存储过程或函数实现传入女神名称，返回：女神 and 男神 格式的字符串
/*
如 传入 ：小昭
返回： 小昭 and 张无忌
*/
CREATE PROCEDURE pro6(IN beautyname VARCHAR(50), OUT str VARCHAR(50))
BEGIN 
	SELECT CONCAT(beautyname, ' and ', IFNULL(boyname, 'null'))
	FROM boys bo 
	RIGHT JOIN beauty b ON b.boyfriend_id = bo.id 
	WHERE b.name = beautyname;
END $

# 创建存储过程或函数，根据传入的条目数和起始索引，查询beauty表的记录
CREATE PROCEDURE pro7(IN size INT, IN startindex INT)
BEGIN
	SELECT * FROM beauty LIMIT startindex, size;
END $
