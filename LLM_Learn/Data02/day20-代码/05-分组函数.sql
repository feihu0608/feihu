# 聚合函数 n条记录 最终会得到1条记录 
# avg() 求平均值
# max() 求最大值
# min() 求最小值
# sum() 求和
# count() 求总数量

# avg(列名) 根据指定列求平均值
# 统计员工表员工平均年龄

select avg(empage) as '平均年龄' from employee;


# 使用四舍五入处理 保留2位小数  
select round(avg(empage),2) as '平均年龄' from employee;


# 统计员工表员工平均薪资

# max(列名) 根据指定列求最大值

# 统计员工表最高薪资

select max(empsalary) from employee;


# 统计员工表最高薪资的员工的  姓名 和 薪资  
# 这里查询最高薪资 但是 没有和后边的 姓名 和 薪资关联
# 所以是将最高薪资和员工表中的第一行数据 一起展示 

select max(empsalary),empname from employee;


# 使用子查询实现 

select empsalary,empname from employee where empsalary = (select max(empsalary) from employee);


# 统计员工表最大年龄

select max(empage) from employee;


# min(列名) 根据指定列求最小值

# 统计员工表最小年龄

select min(empage) as '最小年龄' from employee;


# 统计员工表最低薪资
select min(empsalary) as '最低薪资' from employee;

# count(列名) 统计记录数 

# 统计员工表人数

select count(1) as '总人数' from employee;

select count(*) as '总人数' from employee;

# 统计员工表有多少未成年人 

select count(1) from employee where empage < 18;

# sum(列名) 根据指定列统计总和 

# 统计员工表所有人的年龄总和 

select sum(empage) as '年龄总和' from employee;


# 统计员工表所有人的薪资总和

select sum(empsalary) as '薪资总和' from employee;
