
select * from department;

# 添加数据 

# 方式1 写完整的列名 
insert into department(depid,depname) values(11,'销售部1');

insert into department(depname,depid) values('销售部2',12);

# 方式2 不写列名 值必须跟表中的列的顺序保持一致  

insert into department values(13,'销售部3');
insert into department values('销售部4',14); # 顺序不一致 可能导致类型不匹配 报错 


# 方式3 如果主键为自增 那么可以不添加主键列 
# 注意：这种方式 必须将必填列列名全部书写

insert into department(depname) values('销售部5');


# 方式4 一条SQL语句添加多条记录  

insert into department(depname) 
values('公关部门1'),('公关部门2'),('公关部门3'),('公关部门4'),('公关部门5');












