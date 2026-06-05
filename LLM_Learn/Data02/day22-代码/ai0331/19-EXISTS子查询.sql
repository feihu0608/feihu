# exists 判断子查询是否有结果
# 然后选择是否执行外层的查询   

# 查询员工表是否存在员工信息为null的员工
# 如果存在 则查询部门表的所有数据   

select * from department where exists(select * from employee where empinfo is null);



# not exists 如果子查询没有结果 则执行外层的查询  
select * from department where not exists(select * from employee where empinfo is null);



# 判断员工表是否存在大于60岁的员工  
select * from department where not exists(select * from employee where empage > 60);
