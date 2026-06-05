# 查询所有用户

select * from mysql.user;

# 创建用户 没有密码
create user 'zhaosi';

# 创建用户 并且指定密码 
create user 'dana' identified by 'admin123';


# 授权操作 
grant select,insert on ai0331.account to 'dana';

grant all on ai0331.* to 'zhaosi';



# 撤销权限  
revoke insert on ai0331.account from 'dana';


# 删除用户
drop user 'dana';
drop user 'zhaosi';















