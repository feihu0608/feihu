# 删除 
# delete from 表名 [where condition] 
# 不会清空主键编号 
# delete操作可以回滚(撤销)

# 如果不加条件 会删除表中的全部数据  
delete from department;

# 加条件  
# 删除部门编号大于3的部门
delete from department where depid > 3;


# 等于 删除部门编号为2的部门  

delete from department where depid = 2;


# 回顾in关键字 
# 删除部门编号为1 4 7 的部门   
delete from department where depid in(1,4,7);


# truncate table 表名; 截断表  会删除表中所有的数据  不能加条件  
# 会清空主键编号 即主键会从1开始 
# 不能撤销
truncate table department;

insert into department(depname) value ('技术部');


# drop table 表名;

# drop > truncate > delete 












