# 分组 group by 分组列 
# 分组操作绝大多数场景需要结合聚合函数使用  

# 按照部门编号分组 统计各个部门的平均薪资  

select depid,avg(empsalary) from employee group by depid;

# 按照部门编号分组 统计各个部门的平均薪资 展示部门编号 部门名称 平均薪资 

select department.depid,depname,round(avg(empsalary),2) from employee , department
where employee.depid = department.depid
group by department.depid;


# 统计每个部门的人数 
select depid,count(1) from employee group by depid;

# 按照多列进行分组   分别统计每个部门 男员工 和 女员工的人数
select depid,empsex,count(1) from employee group by depid,empsex;


# 查询每一个部门的平均薪资，显示部门编号，部门的名称，该部门的平均薪资
# 要求，如果没有员工的部门，平均薪资不显示null，显示0

select department.depid,depname,ifnull(avg(empsalary),0) from employee right join department
on employee.depid = department.depid group by department.depid;\


















