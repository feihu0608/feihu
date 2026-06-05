# 双引号或者单引号包含的内容，我们就叫字符串
str1 = "lasidjal;djk"
str2 = "17235"
str3 = 'asukdha12312alskdj'
print(str1,type(str1))

# 1、字符串其实是一个有序的序列，代表这个东西有下标（索引）
print(str2[2],type(str2[2]))
# 2、字符串是一个不能改变的数据类型（不可变类型，说的是容器当中的元素不可变）
# str2[2] = '8'  #错误的 不能改变元素
# 3、字符串是一个容器序列，我们是可以求容器的长度
# print(len(str3))

# 4、字符串和字符串可以相加，拼接字符串
str4 = "我爱你"
str5 = "杨幂"
print(str5 + str4)

# 5、字符串可以使用* ，代表重复多少次，会得到一个新的字符串
str6 = "哈哈"
result = str6 * 6
print(result,id(result),id(str6))
print("*"*50)
print("-"*50)

# 6、字符串的编码（了解）
# ord(单个字符)，逆操作是chr(编码值)函数
str7 = 'c'
print(ord(str7))
num = 98
print(chr(num))

# 如果你想拿到一串字符的编码，直接是没法做到的
# 1、把这个字符串需要自己手动编码
# 2、编码变为字节码后，再去一个一个遍历才能拿到编码的数字
str8 = 'abcdefg'
result = str8.encode("utf-8")
print(result)  #b'abcdefg' 本质上已经把每个字符都变为数字了，只是整体打印是这种字节码形式
# 要想看到编码的数字，只能去遍历一个一个去打印
for num in result:
    print(num)
    print(chr(num))


# 把编码完成的字符串，再去解码变成原来的样子，就是把编码的数字再变回字符串
result1 = result.decode("utf-8")
print(result1)
for char in result1:
    print(char)

# 7、转义字符  \
str9 = "iloveyou\nzhaoliying"
print(str9)
str10 = "iloveyou\tyangmi"
print(str10)
str11 = "adg\\haskj"
print(str11)
str12 = "aks\"jdh"
print(str12)
str13 = "adsd\bgya"
print(str13)
str14 = "asdiuya\rshdiad"
print(str14)

























