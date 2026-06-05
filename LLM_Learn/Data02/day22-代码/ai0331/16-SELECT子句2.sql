# having 用于分组之后过滤 
# 本身的作用和where是相同的


# 查询年龄大于30的人员信息 

select * from employee where empage > 30;
select * from employee having empage > 30;

# 查询每个部门的平均薪资 展示部门编号 部门名称 该部门平均薪资
# 要求如果没有员工的部门 平均薪资不展示null 展示0 
# 只显示平均薪资高于10000的部门信息

select department.depid,depname,ifnull(round(avg(empsalary)),0) from department left join employee
on department.depid = employee.depid group by department.depid
having avg(empsalary) > 10000;


# 查询每个部门的平均薪资超过10000的男员工和女员工的人数  
# 展示人数  性别   部门编号 部门名称 该部门平均薪资 
# 只显示人数大于1人的  部门信息

select department.depid,depname,empsex,count(1),avg(empsalary) from 
employee,department where employee.depid = department.depid
group by department.depid , empsex
having count(1) > 1 and avg(empsalary) > 29000;



















