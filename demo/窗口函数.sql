 窗口函数定义
窗口函数作用于一个数据集合。窗口函数的一个概念就是当前行，
当前行属于某个窗口就是从整个数据集选取一部分数据进行聚合/排名等操作。

窗口函数的语法

window_function_name(window_name/expression)
OVER (
[partition_defintion]
[order_definition]
[frame_definition])

窗口数据集由"[partition_defintion]"，"[order_definition]"，"[frame_definition]"确定。

-- 1. 查询每位学生的成绩总分并排名
--  先找每位同学的总成绩，然后再排名。
select sid,
    name,
    sum(score) as 总成绩,
    RANK() over(
        order by sum(score) desc
    ) 排名
from stuinfo
group by sid
limit 10;
-- 2.查询每个课程的成绩并输出排名列；
select *, DENSE_RANK() OVER(PARTITION BY cid ORDER BY score DESC) 排名
from stuinfo;


-- 聚合函数  avg sum
--3. over后什么都不加
select *, avg(score) over() from stuinfo limit 20;  -- 对所有分数取平均
-- over() 不加参数 数据集为整个数据集


-- 4. over 只加排序参数
select *, avg(score) over(order by score) from stuinfo;
-- 是按成绩升序排列后对成绩进行求平均
-- 1分 134个 2分151个, 2分档的数据 : (134 + 151 * 2) / (151 + 134)
-- select count(1) from stuinfo where score = 2;

-- 5. OVER 分区再加排序
-- 按课程分区,按每门课程分数排序, 对成绩求移动平均
select *, AVG(score) OVER w
from stuinfo
WINDOW w  AS (PARTITION BY cid ORDER BY score);



-- 6. 按平均分数降序排列成绩信息
select *, AVG(score) OVER(PARTITION BY sid) 平均分数 from stuinfo
ORDER BY 平均分数 DESC;


-- 7. 没门课成绩排序,计算与最高分的分差
select *,   (FIRST_VALUE(score) OVER w  - score) AS '分数差'
from  stuinfo
WINDOW w AS (PARTITION BY cid ORDER BY score DESC); 

-- LAG(expr, N, default) 返回滞后于当前行N行的值,没有则为default定义的值
select *,  
 (LAG(score) OVER w  - score) AS '落后前一名分差' ,
 (score - LEAD(score) OVER w) AS '领先后一名分差'
from  stuinfo
WINDOW w AS (PARTITION BY cid ORDER BY score DESC); 

-- frame框架  
select *, 
    LAST_VALUE(score) OVER w
from  stuinfo
WINDOW w AS (PARTITION BY cid ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING); 


--- 基于当前行 前4后2行
select *, 
    min(score) OVER w
from  stuinfo
WINDOW w AS (PARTITION BY cid ROWS BETWEEN 4 PRECEDING AND 2 FOLLOWING); 

