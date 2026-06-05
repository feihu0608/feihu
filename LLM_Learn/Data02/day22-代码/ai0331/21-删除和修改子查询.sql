# 修改技术部 部门的员工薪资为原来的1.5倍  

update employee set empsalary = empsalary * 1.5 where depid = (select depid from department where depname = '技术部')
;

# 修改员工备注信息为null的员工   
# 将其部门编号修改为 技术部的部门编号   
update employee 
set depid = (select depid from department where depname = '技术部') 
where empinfo is null;


# 修改员工表中赵四的薪资 改为 于谦相同的薪资   
# 如果外层的删除和修改 与 内层的查询为统一张表 必须使用临时表处理
# MySQL这样设计是为了避免出现无穷递归  
update employee set empsalary = 
(select empsalary from (select empsalary from employee where empname = '于谦') as temp)
where empname = '赵四';



# 修改员工表 将赵四的薪资 修改为与他所在的部门的平均薪资一致   

update employee set empsalary = 
(select avg_salary from  (select avg(empsalary) as avg_salary  from employee where depid = (select depid from employee where empname = '赵四')) as temp  )
where empname = '赵四';

# 从员工表中 删除 后勤部的员工记录   


delete from employee where depid = (select depid from department where depname = '后勤部')
;



# 删除和赵四同一部门的员工记录   

delete from employee where depid =(select depid from  (select depid from employee where empname = '赵四') as temp)
;






























