# 删除学生表  

drop table student;

create table student(
	sid int primary key auto_increment comment '学生编号',
	sname varchar(20) not null comment '学生姓名',
	sgender char default '男' comment '学生性别',
	sage int not null   comment '学生年龄',
	sidcard varchar(20) not null comment '身份证号',
	check (sage >= 18),
	unique key(sidcard)
);


create table dept(
	did int primary key,		#部门编号
    dname varchar(50)			#部门名称
);

create table emp(
	eid int primary key,  #员工编号
    ename varchar(5),     #员工姓名
    did int,				#员工所在的部门
    foreign key (did) references dept(did)  
    #emp表的deptid和和dept表的did的数据类型一致，意义都是表示部门的编号
    #是否重名没问题，因为两个did在不同的表中
);