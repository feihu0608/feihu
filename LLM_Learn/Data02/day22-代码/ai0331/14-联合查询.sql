# 联合查询



# 内连接 表A inner join 表B on 关联条件  
# 取交集 A∩B 
select * from employee inner join department on employee.depid = department.depid;


# 等值连接  取交集 A∩B  

select * from employee,department where employee.depid = department.depid;


# 查看每个人的姓名 薪资 性别 地址 和 部门编号 以及 部门名称 
# 注意联合的查询的时候 多个表重名字段的问题  
select empname,empsalary,empsex,empaddress,department.depid,depname from employee,department
where employee.depid = department.depid;


# 取别名 给表取别名不要加双引号 或者 单引号 
select empname,empsalary,empsex,empaddress,d.depid,depname 
from employee as e ,department as d
where e.depid = d.depid;


# 左连接 A left join B on  关联条件   
# 展示左表所有行 取交集  右表未匹配的 以null填充 

select * from employee left join department on employee.depid = department.depid;



# 右连接 A right join B on 关联条件  
# 展示右表所有行 取交集 左表未匹配的以null填充   

select * from employee right join department on employee.depid = department.depid;


# 自连接 
# 将一张表当做两张表使用  联合查询  

select * from course;
# 找到关联的条件 进行联合查询(内连接 等值连接)
select c1.profession,c2.cname from course as c1 , course as c2 where c1.cid = c2.profession ;

# union 合并 取多条sql语句的并集  

# 查询年龄大于50的员工信息  

# 查询年龄小于18的员工信息 
select * from employee where empage > 50

union

select * from employee where empage < 18;


# 如果两条SQL查询的列的数量不一致 会报错
# 如果数量一致 但是内容不一致 不报错 但是不能解决任何问题 
select empsalary,empaddress from employee where empage > 50
union
select empname,empage from employee where empage < 18;


# 查询薪资大于10000的人员信息 union 不会保存重复记录   
select * from employee where empsalary > 10000
union
select * from employee where empsex = '女';



# union all 和 union 的区别 只有一个 union all 会保存重复记录


select * from employee where empsalary > 10000
union all
select * from employee where empsex = '女';












