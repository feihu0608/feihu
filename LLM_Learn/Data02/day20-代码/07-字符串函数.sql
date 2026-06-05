# ------------------------------------------------
# 字符串函数 
# concat() 拼接

select concat('a','abc','你好','hello');

# 将员工的姓名和地址拼接在一起 

select concat(empname,empaddress) from employee;
select concat_ws(':',empname,empaddress) from employee;


# concat_ws() 使用指定字符拼接指定的内容  
select concat_ws('#','a','b','c');


# char_length() 返回字符数  

select char_length('abc');
select char_length('世界你好');

# 统计每个人的姓名包含几个字符  
select empname,char_length(empname) from employee;


# length() 返回字节数  

select length('abc');
select length('世界你好');


# upper() 转换为大写  
select upper('abc');
select upper('123');
select upper('世界你好');

# lower() 转换为小写 
select lower("AbCEdf");

# reverse() 翻转字符串 前后顺序颠倒
select reverse("AbCEdf");


# trim() 去除前后的空格 

select trim(' a b c d e  ');
select length(trim(' a b c d e  '));

# replace() 

select replace('abc abc','a','A');
select replace(' a b c d e  ',' ','');

# LEFT（s，n）函数表示取字符串s最左边的前n个字符
select left('abc',3);
select left('abc',2);
select left('abc',1);

# 右填充 不满足指定位数 以指定的符号填充 
select rpad('a',3,'*');



#（2）在“employee”表中查询薪资高于15000的男员工姓名，
#并把姓名处理成“张xx”的样式。
SELECT  RPAD(LEFT(empname,1),3,'*'),empsalary
FROM employee
WHERE empsalary>15000 AND empsex ='男';


# 截取字符串  从第1个位置开始 截取前5个 
select substr('abc hello world',1,5);
select substring('abc hello world',1,5);

# 找指定的内容在字符串中 第一次出现的位置  
select position('h' in 'abc abc hello');

# 查找@符号 在邮箱中 出现的位置 返回的序号 
select position('@' in empemail) from employee;


# 查询姓名 邮箱 以及 邮箱@之前的内容 筛选薪资大于10000 并且 性别为 男   
SELECT empname,empemail,
SUBSTRING(empemail,1, POSITION('@' IN empemail) -1)
FROM employee
WHERE empsalary > 10000 AND empsex ='男';



SELECT TRIM('    hello   world   '); #默认是去掉前后空白符
SELECT CONCAT('[',TRIM('    hello   world   '),']'); #默认是去掉前后空白符
SELECT TRIM(BOTH '&' FROM '&&&&hello   world&&&&'); #去掉前后的&符号
SELECT TRIM(LEADING '&' FROM '&&&&hello   world&&&&'); #去掉开头的&符号
SELECT TRIM(TRAILING '&' FROM '&&&&hello   world&&&&'); #去掉结尾的&符号








