# 创建表 复制表结构 
create table 表名 like 表名;
create table dep like department;
create table emp like employee;

# 复制数据
insert into 表名(select …… );
insert into dep  (select * from department);
insert into emp  (select * from employee);


# 创建表 同时 复制结构数据
create table 表名 as(select …… );
create table d as (select * from department);