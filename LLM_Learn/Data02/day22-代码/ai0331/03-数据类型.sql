# 整数类型 

create table t_int(
	i1 int,
	i2 int(5) unsigned zerofill 
);


drop table t_int;


insert into t_int(i1,i2) values(1234,1234);
insert into t_int(i1,i2) values(12345,12345);
insert into t_int(i1,i2) values(12345,666666666);

select * from t_int;

# bit 类型 位类型 默认不指定宽度 只能存1位二进制数 指定位数 则可以保存对应位数的二进制


create table t_bit(
	b1 bit,
	b2 bit(4)
);


insert into t_bit(b1,b2) values(1,1);

select * from t_bit;


# 浮点类型  

create table t_double(
	d1 double,
	d2 double(5,2)  # -999.99 ~ 999.99
);

insert into t_double(d1,d2) values(2.5,2.5);
insert into t_double(d1,d2) values(2.5,222.555);
insert into t_double(d1,d2) values(2.5,2222.555);# 报错 整数部分超出范围



select * from t_double;



# decimal类型 精确的浮点数  

create table t_decimal(
	d1 decimal,  # 如果不指定(M,D) 默认为(10,0)
	d2 decimal(5,2)
);


insert into t_decimal(d1,d2) values(1.5,2.5); # 第一列不能保存小数 整数部分根据小数四舍五入
insert into t_decimal(d1,d2) values(1.4,2.5);

select * from t_decimal;

# 字符串类型 
# char类型
create table t_char(
	c1 char, # 如果不指定宽度 默认只能存一个字符
	c2 char(3) # 最多可以保存3个字符  
);


insert into t_char value('A','abc');
insert into t_char value('abc','abc'); #报错 因为第一列超出长度
insert into t_char value('a','ac e'); #报错 因为第二列超出长度
insert into t_char value('中','世 你'); #报错 因为第二列超出长度


select * from t_char;




# varchar类型
create table t_varchar(
	v1 varchar(3)
);

insert into t_varchar(v1) values("abc");
insert into t_varchar(v1) values("中文汉");
insert into t_varchar(v1) values("123");
insert into t_varchar(v1) values("   ");
insert into t_varchar(v1) values("abcd"); # 报错 超出长度


# 枚举和集合类型 

create table t_enum_set(
	gender enum("男","女"),
	hobby set("唱","跳","RAP","篮球")
);


insert into t_enum_set(gender,hobby) values("男","唱,跳,RAP"); 
insert into t_enum_set(gender,hobby) values("你","唱,跳,RAP");  # 报错 性别错误
insert into t_enum_set(gender,hobby) values("男","唱,跳,游泳"); # 报错 爱好错误



# text  类型

create table t_text(
	t1 text
);

insert into t_text values("今天很开心 哈哈哈哈");




# 二进制字符串类型 比如可以存储字节流对应的数据  

create table t_binary(
	b1 binary, #没有指定(M)，默认是(1)
	b2 varbinary(10) #没有指定(M)，报错，必须指定(M)
);

insert into t_binary
values('a','a');

insert into t_binary
values('A','B');


select * from t_binary;


# blob 类型 或者 longblob 等类型 用于存储二进制的大对象 

create table t_blob(
	t1 blob
);


select * from t_blob;


# 日期类型 
# 只保留年份  
create table year_temp(
	d year
);

insert into year_temp values(2021);
insert into year_temp values(85);
insert into year_temp values(22);
insert into year_temp values(69);
insert into year_temp values(0);
insert into year_temp values('0');

select * from year_temp;


# 时间戳 和 datetime类型  

create table t_t(
	t1 datetime,
	t2 timestamp
);

insert into t_t(t1,t2) values('2012-12-12 10:10:10','2012-12-12 10:10:10');
insert into t_t(t1,t2) values('20121212101010','20121212101010');
insert into t_t(t1,t2) values('2012&12&12& 10#10#10','2012&12&12& 10#10#10');
insert into t_t(t1,t2) values('2012121211010','2012121211010'); # 报错 因为后边的位数不够 















