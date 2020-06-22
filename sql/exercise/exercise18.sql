/*
1、已知表stringcontent
其中字段：
id 自增长
content varchar(20)
向该表插入指定个数的，随机的字符串
*/

CREATE TABLE stringcontent(
    id INT PRIMARY KEY AUTO_INCREMENT,
    content VARCHAR(20)
);

DECLARE $
CREATE PROCEDURE p1(IN num INT)
BEGIN 
    DECLARE i INT DEFAULT 0;
    DECLARE str VARCHAR(26) DEFAULT 'abcdefghijklmnopqrstuvwxyz';
    DECLARE startindex INT DEFAULT 1;
    DECLARE len INT DEFAULT 1;
    WHILE i<num DO
	
	SET startindex = FLOOR(RAND() * 26 + 1);
	SET len = FLOOR(RAND()*(20 - startindex + 1) + 1);
	INSERT INTO stringcontent(content) VALUES(SUBSTR(str, startindex, len));
	SET i = i + 1;
   END WHILE;
END $

CALL p1(10)$
