# 判断员工的年龄 如果 小于18则显示未成年 否则显示成年  

select empname,empage,if(empage >= 18,'成年','未成年') as '是否成年' from employee;


# 判断员工的备注信息是否为null 如果是则展示 '这个人很懒 什么都没留下' 否则 展示个人信息  

select * from employee;

select empname,ifnull(empinfo,'这个人很懒 什么都没留下') as '员工信息' from employee;


# 相当于Python中的多重if  
# 查询员工表 名字 年龄 以及年龄所属的阶段  

select empname,empage,
case 
	when empage > 50 then '老年'
	when empage > 40 then '中年'
	when empage > 30 then '青年'
	when empage >=18 then '成年'
	else '未成年' end as '年龄阶段'
from employee;


# 相当于Python中 match-case
# 查询员工表 姓名 部门编号  根据部门编号 展示部门名称  
select empname,depid,
case depid
when 1 then '技术部'
when 2 then '后勤部'
when 3 then '财务部'
when 4 then '人事部'
else '其他部门' end as '部门名称'
from employee;





