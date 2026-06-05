create table stu(
	stuid int,
	stuname varchar(20)
);


# 修改表结构 统一以 alter table 开头  

# 添加主键约束
alter table stu add primary key(stuid);

# 添加唯一约束 
alter table stu add unique key(stuname);


# 删除唯一约束
alter table stu drop index stuname;



# 删除主键约束
alter table stu drop primary key;

# 修改列的信息 删除了不要的信息  原来有not null 现在没有了  
alter table stu modify stuid int;

# 修改列增加想要的信息
alter table stu modify stuid int primary key auto_increment comment '学生编号';


# 新增列  
alter table stu add age int;


# 给年龄列新增检查约束 

alter table stu add check(age >= 20);


# 删除检查约束 
alter table stu drop check stu_chk_1;

# 修改表名 
alter table stu rename to s;

rename table s to stu;


# 删除列  
alter table stu drop column age;


# 修改列名 以及修改属性  
alter table stu change stuname sname varchar(100);


# 添加字段  
# 可以执行字段(Field 列)在哪个位置  

alter table stu add aid int first;

select * from stu;


alter table stu add bid int after aid;
















create table test_pri(
	id int primary key auto_increment comment '主键列',
	name varchar(20)
);


# 删除主键 
# 因为auto_increment必须作用在键上 所以必须先撤销auto_increment
alter table test_pri modify id int;

# 然后再删除  
alter table test_pri drop primary key;






















