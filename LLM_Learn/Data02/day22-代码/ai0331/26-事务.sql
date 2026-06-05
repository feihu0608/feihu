# ACID特性
#（1）**原子性（Automicity）**
#原子性是指事务是一个不可分割的工作单位，事务中的操作要么都发生，要么都不发生。 

#（2）**一致性（Consistency）**
#事务必须使数据库从一个一致性状态变换到另外一个一致性状态。

#（3）**隔离性（Isolation）**
#事务的隔离性是指一个事务的执行不能被其他事务干扰，即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。

#（4）**持久性（Durability）**
#持久性是指一个事务一旦被提交，它对数据库中数据的改变就是永久性的，接下来的其他操作和数据库故障不应该对其有任何影响

drop table account;
create table account(
	id int primary key auto_increment,
	name varchar(20) not null,
	money decimal not null
);

insert into account (name,money) values ('赵四',5000),('大拿',5000);




# 开启事务 接下来执行的DML语句 不会自动提交 必须手动提交  
# 这个操作也属于关闭自动提交  
start transaction;
select * from account;

update account set money = money - 1000 where id = 1;

update account set money = mony + 1000 where id = 2;



# 不管最终是提交或者回滚 事务都将结束 
# 提交 数据将持久化 即无法回滚
commit;

# 回滚 回滚到事务执行之前的状态  
rollback;




# 事务有四种隔离级别 不同的隔离级别会对应不同的现象  
# READ-UNCOMMITTED 读未提交 当前事务可以读取到其他事务未提交的数据 					脏读 不可重复读 幻读  
# READ-COMMITTED  读已提交 当前事务可以读取到其他事务已提交的数据 							不可重复读 幻读
# REPEATABLE-READ 可重复读 当前事务可以保证多次相同的DQL操作 结果始终保持一致   幻读
# SERIALIZABLE 串行化 、串读 不会有任何问题 但是多个事务操作同样的数据 需要排队执行  

# 默认的隔离级别属于REPEATABLE-READ 可重复读

# 查看隔离级别
select @@transaction_isolation;


# 修改事务的隔离级别
set transaction_isolation = 'READ-UNCOMMITTED';
set transaction_isolation = 'READ-COMMITTED';
set transaction_isolation = 'REPEATABLE-READ';
set transaction_isolation = 'SERIALIZABLE';



# SERIALIZABLE 串行化 串读  
# A事务隔离级别设置为SERIALIZABLE  B事务隔离级别设置为REPEATABLE-READ
# A查询 B修改 B要排队 
# B修改 A查询 A要排队  
# A查询 B查询 不排队  
# A修改 B查询 不排队 

















