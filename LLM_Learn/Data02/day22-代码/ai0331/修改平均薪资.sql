

update employee set empsalary = 
(select avg_salary from (select avg(empsalary) as avg_salary from employee)as temp1) 
where depid = (select depid from (select depid from employee where empname = '赵四')as temp2);

