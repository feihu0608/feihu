# 排序
# order by  数值列名 

# 查询员工表 按照薪资 升序排列  

select * from employee order by empsalary;

# asc表升序 默认不写也是升序  
select * from employee order by empsalary asc;


# 查询员工表 按照薪资 降序排列  
select * from employee order by empsalary desc;



# 查询员工表 按照年龄 升序排列  

select * from employee order by empage;


select * from employee order by empage desc;

# limit 用于分页展示数据  
# limit n  展示前n条数据 

select * from employee limit 5;


# limit j,k  从j + 1 条开始展示 展示k条数据 
# 页容量 = 10 
# 页码 = 1 
# j = (页码 - 1 ) * 页容量     k = 页容量

select * from employee limit 0,10;
select * from employee limit 10,10;
select * from employee limit 20,10;


# 查询员工表前三名薪资最高的员工信息  

select * from employee order by empsalary desc limit 3;

























