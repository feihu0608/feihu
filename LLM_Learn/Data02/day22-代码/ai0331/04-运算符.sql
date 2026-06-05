# 算数运算符 

select 1 + 3;
select 1 + 3 , 1 -2 , 1 * 2 , 1 / 2 ,10 % 3;

# 使用as关键字给列取别名

select 1 + 3 as '求和' , 1 -2 as '求差' , 1 * 2 as '求积' , 1 / 2 as '求商' ,10 % 3 as '取余';

# as关键字可以省略 但是不推荐省略
select 1 + 3  '求和' , 1 -2  '求差' , 1 * 2  '求积' , 1 / 2  '求商' ,10 % 3  '取余';
select 1 + 3  求和 , 1 -2  求差 , 1 * 2  求积 , 1 / 2  求商 ,10 % 3  取余;
select 1 + 3  sum , 1 -2  求差 , 1 * 2  求积 , 1 / 2  求商 ,10 % 3  取余;


# 关系运算符 
# 查询员工表所有数据

select * from employee;


# 查询未成年的员工的姓名和年龄

select empname,empage from employee where empage < 18;

# 查询薪资大于15000的员工信息

select * from employee where empsalary > 15000;

 
# 查询部门编号为1的员工信息

select * from employee where depid = 1;


# 查询部门编号不为1的员工信息

select * from employee where depid != 1;


# ------------------------------------------------


# = 和  != 不能用于null值的判断  
# is null  用于判断为null值
# is not null  用于判断不为null值  

# 查询员工备注信息为null的员工  

select * from employee where empinfo is null;


# 查询员工备注信息不为null的员工 

select * from employee where empinfo is not null;

# between start  and  end 

# 查询年龄在18 到 45 岁之间的人员信息 

select * from employee where empage >= 18 and empage <= 45;

select * from employee where empage >= 18 && empage <= 45;

select * from employee where empage between 18 and 45;



# 查询年龄不在18 到 45 岁之间的人员信息 

select * from employee where empage < 18 or empage > 45;

select * from employee where empage < 18 || empage > 45;

select * from employee where empage not between 18 and 45;



# 查询部门编号为1/2/3的人员信息

select * from employee where depid = 1 or depid = 2 or depid = 3;


# 使用in关键字实现 in关键字后边 应该加上一个数据集合  

select * from employee where depid in(1,2,3);


# 查询部门编号不为1/2/3的人员信息

select * from employee where depid not in(1,2,3);


# 模糊查询 
# like  
#  %  表示任意个数任意字符 
#  _  表示一个任意字符 

# 查询名字中包含'赵'的人员信息

select * from employee where empname like '%赵%';


# 查询名字以'赵'开头的人员信息

select * from employee where empname like '赵%';

# 查询名字以'赵'结尾的人员信息

select * from employee where empname like '%赵';

# 查询名字以'赵'开头的人员信息 并且名字只有两个字的人员信息


select * from employee where empname like '赵_';


# 查询名字以'赵'开头的人员信息 并且名字只有三个字的人员信息

select * from employee where empname like '赵__';

# 逻辑运算符
#查询薪资高于15000，并且性别是男的员工

select * from employee where empsalary > 15000 && empsex = '男';


#查询薪资高于15000，或者depid为1的员工


select * from employee where empsalary > 15000 or depid = 1;


#查询薪资不在[15000,20000]范围的

select * from employee where empsalary < 15000 or empsalary > 20000;


# xor  查询薪资高于15000，或者depid为1的员工，两者只能满足其一

select * from employee where empsalary > 15000 xor depid = 1;


# 位运算符
select 1 << 2;
select 4 >> 1;








