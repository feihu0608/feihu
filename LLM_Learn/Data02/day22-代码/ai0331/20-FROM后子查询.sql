# 查询每个部门的员工总薪资 返回部门名称 和 对应的总薪资  
select depname,sum(empsalary) from employee,department
where employee.depid = department.depid group by department.depid;

# 使用子查询的方式写  
# 先书写子查询将部门的总薪资查询出来 然后再结合外层的查询 

select depname,sum_salary from department,
(select depid,sum(empsalary) as sum_salary from employee group by depid) as temp
where department.depid = temp.depid;

