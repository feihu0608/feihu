# 查询薪资最高的人的姓名 年龄 和薪资   
select empname,empage,empsalary from employee where empsalary =  (select max(empsalary) from employee);

select empname,empage,empsalary from employee order by empsalary desc limit 1;

# 查询每个人的姓名 年龄 薪资 公司的平均薪资  

# 错误结果 只剩下一条记录
select empname,empage,empsalary,avg(empsalary) from employee;

# 使用子查询实现 

select empname,empage,empsalary,(select round(avg(empsalary)) from employee) from employee;


# 查询每个人的姓名 年龄 地址  薪资 和 公司平均薪资的差值  
# 并显示个人的薪资和公司的平均薪资差值 大于15000以上的记录  

select empname,empage,empaddress,empsalary,
(select avg(empsalary) from employee) as '公司的平均薪资',
abs(empsalary - (select avg(empsalary) from employee)) as '差值'
from employee
where abs(empsalary - (select avg(empsalary) from employee)) > 15000;

# 查询年龄最大的人的姓名 年龄 和 地址    

select empname,empage,empaddress from employee where empage =(select max(empage) from employee);

# 查询比 赵四 赵云 小宝 这三个人 薪资都高的人员信息  

select * from employee where empsalary > (select max(empsalary) from employee where empname in ('赵四','赵云','小宝'));

select * from employee 
where empsalary > all(select empsalary from employee where empname in ('赵四','赵云','小宝'));


# 查询比全公司的平均薪资高的男员工的姓名和薪资  

select empname,empsalary from employee
where empsalary > (select avg(empsalary) from employee) and empsex = '男';

# 查询和 赵四 云姨 同一个部门的人员姓名 地址 部门编号  

select empname,empaddress,depid from employee where depid in (select depid from employee where empname in ('赵四','云姨'));



# 查询员工表以及部门表  按照部门统计平均薪资  
# 显示部门的平均薪资比全公司的平均薪资高的部门编号 部门名称 部门平均薪资
# 并且按照部门平均薪资升序排列  

select department.depid,depname,avg(empsalary),(select avg(empsalary) from employee) from employee,department
where employee.depid = department.depid group by department.depid
having avg(empsalary) > (select avg(empsalary) from employee) 
order by avg(empsalary);
 












































