# CTE属于通用表达式 作用于当前查询 可以复用 也可以递归  


# 统计每个部门的人数 展示部门编号 名称 和部门人数    
with temp as (
	select depid,count(*) as emp_count
	from employee group by depid
)
select d.depid,d.depname,t.emp_count from department as d  inner join temp as  t
on d.depid = t.depid;


# 查询薪资大于8000的员工姓名 薪资  部门名称  

with temp as (
	select * from employee where empsalary > 8000
)
select d.depid,depname,empsalary from department as d  inner join temp as t
on d.depid = t.depid;


# 递归操作  
with recursive temp as(
	select 1 as n 
	union all 
	select n + 1
	from temp 
	where n < 6
)
select depid,depname,temp.n from department inner join temp 
on department.depid = temp.n;




