select * from department;

# 修改  
# update 表名 set 列名1 = 值1 , 列名2 = 值2 …… [where condition];

# 不加条件
update department set depname = '销售部';


# 加条件 只针对于符合条件的行生效 
# 修改编号为1的部门 名称为 安保部  
update department set depname = '安保部' where depid = 1;


# 一次修改多列  
# 修改赵四的薪资为50000元 性别改为女   地址改为北京 
select * from employee;

update employee set empsalary = 50000,empsex = '女' , empaddress = '北京' where empname = '赵四';


# 修改部门编号为1的员工 薪资改为30000

update employee set empsalary = 30000 where depid = 1;
















