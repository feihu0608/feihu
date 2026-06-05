# 查询每个人的姓名 薪资 和 公司的平均薪资

select empname,empsalary,(select round(avg(empsalary),2) from employee) from employee;


# 查询每个人的姓名 薪资 和 每个部门的平均薪资
select empname,empsalary,(select round(avg(empsalary),2) from employee group by depid) from employee;


# 以上问题可以通过窗口函数解决  

select depid,empname,empsalary,avg(empsalary) over(partition by depid) as '部门平均薪资' from employee;



# 查询员工表 每个人的姓名 薪资 和 每个部门的平均薪资
# 各自部门按照薪资升序排列 分别使用三种函数
# row_numer()  rank()  dense_rank()

select depid,empname,empsalary,avg(empsalary) over(partition by depid) as '部门平均薪资',
row_number() over(partition by depid order by empsalary) as 'row_number',
rank() over(partition by depid order by empsalary) as 'rank',
dense_rank() over(partition by depid order by empsalary) as 'dense_rank'
from employee;



select depid,empname,empsalary,avg(empsalary) over(partition by depid) as '部门平均薪资',
row_number() over w as 'row_number',
rank() over w as 'rank',
dense_rank() over w as 'dense_rank'
from employee window w as (partition by depid order by empsalary);








update employee set empsalary = 7500 where empname = '四小赵';







# 查询每个人的薪资排名的上一位 下一位 首位 末位的信息  

select empname,empsalary,
lag(empname,1,'-') over(order by empsalary) as '上一位的姓名',
lag(empsalary,1,0) over(order by empsalary) as '上一位的薪资',
lead(empname) over(order by empsalary) as '下一位的姓名',
lead(empsalary) over(order by empsalary) as '下一位的薪资',
first_value(empsalary) over(order by empsalary) as '首位薪资',
last_value(empsalary) 
# 从第一行到最后一行统计 
over(order by empsalary rows between unbounded preceding and unbounded following) as '末位薪资'
from employee;






























