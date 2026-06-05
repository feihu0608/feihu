# 数学函数属于单行函数 即原本多少条记录 计算完以后 记录数不变 

# 绝对值
select abs(-123);

# 向上取整
select ceil(3.3);

# 向下取整
select floor(3.9);

# 四舍五入
select round(3.5);
select round(3.4);


# 随机数 0 ~ 1 之间的随机小数 包括0不包括1 
select rand();


# 截断小数位  保留指定位数的小数
select truncate(3.339333,2);

# 格式化数值  

select format(2659652641,3);


# 平方根
select sqrt(9);


# 次幂 
select pow(2,3);


#在“employee”表中查询员工无故旷工一天扣多少钱，
#分别用CEIL、FLOOR、ROUND、TRUNCATE函数。
#假设本月工作日总天数是22天，
#旷工一天扣的钱=salary/22。
SELECT empname,empsalary/22,CEIL(empsalary/22),
FLOOR(empsalary/22),ROUND(empsalary/22,2),
TRUNCATE(empsalary/22,2) FROM employee; 


#查询公司平均薪资，并对平均薪资分别
#使用CEIL、FLOOR、ROUND、TRUNCATE函数
SELECT AVG(empsalary),CEIL(AVG(empsalary)),
FLOOR(AVG(empsalary)),ROUND(AVG(empsalary),2),
TRUNCATE(AVG(empsalary),2) FROM employee;















