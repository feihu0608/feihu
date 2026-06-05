# 日期函数
# 获取当前系统日期

select curdate(),current_date();

# 获取当前系统日期
select curtime(),current_time();

# 获取年月日时分秒
SELECT CURRENT_TIMESTAMP(),LOCALTIME(),SYSDATE(),NOW();


# 获取UTC日期时间
select utc_date(),utc_time(),curdate(),curtime();


# 获取时间戳 从1970年1月1日0点0分0秒到目前的秒钟 
SELECT UNIX_TIMESTAMP(),UNIX_TIMESTAMP('2012-12-12');


# 将时间戳转换为日期 
 SELECT FROM_UNIXTIME(1777512123);
 
 
# 获取对应的信息 比如 年 月 日    
select year(curdate()),month(curdate()),day(curdate());

# 获取对应的信息 比如 时分秒  
select hour(curtime()),minute(curtime()),second(curtime());



# 统计两个日期的间隔天数 
# 统计现在到七夕还有多少天   
select datediff('2026-07-07',now());


# 统计现在到放学还有多长时间  
select timediff('17:30:00',CURRENT_TIME());

# 查询员工表 本月过生日的员工 

select * from employee where month(empbirthday) = month(curdate());























 
 
 
 
 
 
 








