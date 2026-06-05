# | **函数**                       | **说明**                                                     |
# | ------------------------------ | ------------------------------------------------------------ |
# | **str.replace(old,new[,max])** | 把将字符串中的old替换成new,如果指定max，则替换不超过max次    |
str1 = "abcdefg"   #***************
result = str1.replace("de","haha")
print(str1,result)


# | **str.split([x][,n])**         | 按x分隔字符串，默认按任何空白字符串分隔并在结果中丢弃空字符串。可指定最大分隔次数 |
str1 = "a bc-bcd-haha-hehe"  #****************
# result = str1.split("") #不能是空串
# result = str1.split() #默认以空格去作为切割符
result = str1.split("-") #以指定的子串为切割符
print(str1,result)



# | **str.rsplit([x][,n])**       | 与split()类似，从右边开始分隔
str1 = "haha abc-bcd-haha-hehe hehe"
result = str1.rsplit() #********************
print(str1,result)
#
#
# |
# | **x.join(seq)**                | 以x作为分隔符，将序列中所有的字符串合并为一个新的字符串      |
str1 = "**"
list1 = ["杨幂","赵丽颖","迪丽热巴"]
result = str1.join(list1)  #******************
print(str1,result)




# | **str.strip([x])**             | 截掉字符串两边的空格或指定字符                               |
str1 = "    abcd    "
str2 = "zhaoliying zhao abcdliyingzhao"
# result = str1.strip()
result = str2.strip("zhao") #********************
print(str2)
print(result)


# | **str.lstrip([x])**            | 截掉字符串左边的空格或指定字符                               |
str1 = "    askjdhasd    "
result = str1.lstrip()
print(str1)
print(result)

# | **str.rstrip([x])**            | 截掉字符串右边的空格或指定字符                               |
result = str1.rstrip()
print(str1)
print(result)


# | **str.removeprefix()**         | 截掉字符串指定前缀                                           |
str1 = "prezhaoliyingpre"
result = str1.removeprefix("pre")
print(str1)
print(result)


# | **str.removesuffix()**         | 截掉字符串指定后缀

result = str1.removesuffix("pre")
print(str1)
print(result)


# | **str.upper()**                | 将所有字符转为大写                                           |
str1 = "asjkdhasA123789467djkjh"
result = str1.upper()  #**************
print(str1)
print(result)


# | **str.lower()**                | 将所有字符转为小写
result = str1.lower() #******************
print(str1)
print(result)



# | **str.swapcase()**                  | 反转字符串中字母大小写                                       |
str1 = "asdghajABCD1132123"
result = str1.swapcase()
print(str1)
print(result)


# | ----------------------------------- | ------------------------------------------------------------ |
# | **str.capitalize()**                | 将字符串第一个字母变为大写，其他字母变为小写                 |
str1 = "asdADHGJ12938271jksdfhsjk"
result = str1.capitalize()   #***************
print(str1)
print(result)


# | **str.title()**                     | 将字符串每个单词首字母大写,以空白（空格 制表符 换行符）计算单词                                   |
str1 = "sdha\tksasd"
result = str1.title()
print(str1)
print(result)

# | **str.find(x[,start][,end])**       | 返回字符串中第一个x的索引值，不存在则`返回-1`，可指定字符串开始结束范围 |
# | **str.index(x[,start][,end])**      | 返回字符串中第一个x的索引值，不存在则`报错`，可指定字符串开始结束范围 |
str1 = "asjkdaslkdjasdk"
result = str1.find("赵丽颖") #**********************
result = str1.find("sdk")
print(str1)
print(result)

# result = str1.index("赵丽颖")
# print(str1)
# print(result)

# 注意：后期在长串当中找子串的下标其实 find用的比较多，因为他找的时候安全 而且可以根据返回结果判断





# | **str.rfind(x[,start][,end])**      | 与find()类似，从右边开始查找                                 |
# | **str.rindex(x[,start][,end])**     | 与index()类似，从右边开始查找                                |
str1 = "asghda赵丽颖asjkdha赵丽颖sdklfjasldk赵丽颖"
# result = str1.rfind("赵丽颖")
result = str1.rfind("杨幂")
print(str1)
print(result)

result = str1.rindex("赵丽颖")
# result = str1.rindex("杨幂")
print(str1)
print(result)




# | **str.startswith(x[,start][,end])** | 检查字符串是否以x开头，可指定字符串开始结束范围              |
str1 = "yangmiaksdjaskhahaalskdj"
result = str1.startswith("aa")  #********************
result = str1.startswith("yangmi")
print(str1)
print(result)





# | **str.endswith(x[,start][,end])**   | 检查字符串是否以x结尾，可指定字符串开始结束范围              |
str1 = "asjkldjasdkljayangmi"
result = str1.endswith("yangmi")
print(str1)
print(result)



# | **str.isspace()**                   | 检查字符串是否非空且只包含空白(空格 制表\t  换行\n不包含空串，空串不是空白)                               |
str1 = "\n"
result = str1.isspace()
print(str1)
print(result)




# 其它字符串方法
# center() 方法返回一个指定宽度并居中对齐的字符串，两侧使用指定字符填充
text = "hello"
centered_text = text.center(15, '*')
print(f"'{text}' 居中对齐(宽度15,填充*) = '{centered_text}'")

# 使用默认空格填充
centered_default = text.center(15)
print(f"'{text}' 居中对齐(宽度15,默认填充) = '{centered_default}'")



# ljust() 方法返回一个指定宽度并左对齐的字符串，右侧使用指定字符填充
text = "hello"
left_justified = text.ljust(15, '-')
print(f"'{text}' 左对齐(宽度15,填充-) = '{left_justified}'")

# 使用默认空格填充
left_default = text.ljust(15)
print(f"'{text}' 左对齐(宽度15,默认填充) = '{left_default}'")

# rjust() 方法返回一个指定宽度并右对齐的字符串，左侧使用指定字符填充
text = "hello"
right_justified = text.rjust(15, '.')
print(f"'{text}' 右对齐(宽度15,填充.) = '{right_justified}'")

# 使用默认空格填充
right_default = text.rjust(15)
print(f"'{text}' 右对齐(宽度15,默认填充) = '{right_default}'")





# zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0
number = "42"
zero_filled = number.zfill(8)
print(f"'{number}' 用0填充到长度8 = '{zero_filled}'")


# 对于负数，负号会在0之前
negative_number = "-42"
negative_zero_filled = negative_number.zfill(8)
print(f"'{negative_number}' 用0填充到长度8 = '{negative_zero_filled}'")


# splitlines() 方法按照行('\r', '\n', '\r\n')分割字符串，返回包含各行的列表
# print("asjkdah\r\nasjkhda")


multiline_text = """第一行
第二行
第三行"""

lines = multiline_text.splitlines()
print(f"原始多行文本:\n{multiline_text}")
print(f"splitlines() 分割结果 = {lines}")

# keepends=True 保留换行符
lines_with_endings = multiline_text.splitlines(True)
print(f"splitlines(True) 分割结果 = {lines_with_endings}")



# partition() 方法从左边开始查找分隔符，将字符串分割成三部分：分隔符前、分隔符、分隔符后
text = "hello-world-python"
partition_result = text.partition('-')
print(f"'{text}' 以 '-' 分割 = {partition_result}")

# 如果找不到分隔符，则返回 (原字符串, '', '')
no_separator = "helloworld"
partition_no_match = no_separator.partition('-')
print(f"'{no_separator}' 以 '-' 分割 = {partition_no_match}")
#
# rpartition() 方法从右边开始查找分隔符，将字符串分割成三部分：分隔符前、分隔符、分隔符后
text = "hello-world-python"
rpartition_result = text.rpartition('-')
print(f"'{text}' 从右以 '-' 分割 = {rpartition_result}")
#
# 如果找不到分隔符，则返回 ('', '', 原字符串)
no_separator = "helloworld"
rpartition_no_match = no_separator.rpartition('-')
print(f"'{no_separator}' 从右以 '-' 分割 = {rpartition_no_match}")



# **str.expandtabs([tabsize])**将字符串中\t转化为空格，可指定每个\t空格数
# 默认\t使用这个方法后空格数是8
# 而我们可以指定使用这个方法后让\t变为几个空格
str1 = "ajkaskld\tjasd'lad"
result = str1.expandtabs(2)
print(str1)
print(result)


# format_map() 方法使用字典作为参数来格式化字符串
template = "姓名: {name}, 年龄: {age}, 城市: {city}"
data = {"name": "张三", "age": 25, "city": "北京"}
formatted_text = template.format_map(data)
print(f"模板字符串: {template}")
print(f"字典数据: {data}")
print(f"format_map 格式化结果: {formatted_text}")

# 与 format() 的区别：format_map 直接接受字典
another_template = "课程: {course}, 成绩: {score}"
course_data = {"course": "Python", "score": 95}
result = another_template.format_map(course_data)
print(f"课程信息格式化: {result}")

str1 = "课程: {course}, 成绩: {score}"
result = str1.format(course = "语文",score = 100)
print(str1,result)




# | **str.isdecimal()** | 检查字符串是否非空且只包含十进制字符 |
str1 = "1023"
result = str1.isdecimal()
print(str1)
print(result)


# | **str.isdigit()**   | 检查字符串是否非空且只包含数字       |
str1 = "1101"
result = str1.isdigit()
print(str1)
print(result)



str1 = "AASUGH123SJK"
result = str1.isupper()
print(str1)
print(result)
str1 = "一"


result = str1.isnumeric()
print(str1)
print(result)


str1 = "sdhaksdh"
result = str1.isprintable()
print(str1)
print(result)

str1 = "Asjkdh"
result = str1.istitle()
print(str1)
print(result)



# 翻译
translation_dict = {'h': 'H', 'l': 'L', 'o': 'O'}
dict_table = str.maketrans(translation_dict)
simple_text = "hello"
dict_translated = simple_text.translate(dict_table)
print(f"\n原文本: {simple_text}")
print(f"字典映射: {translation_dict}")
print(f"翻译后: {dict_translated}")

# # 两个参数版本：str1 中的字符映射到 str2 中对应位置的字符  str2当中的字符后期会一一对应去替换str1当中的每个字符
str1 = "abc"
str2 = "123"
translation_table = str.maketrans(str1, str2)
original_text = "bacadb"
translated_text = original_text.translate(translation_table)
print(f"原文本: {original_text}")
print(f"映射规则: {str1} -> {str2}")
print(f"翻译后: {translated_text}")
#
# 三个参数版本：第三个参数是要删除的字符
str1 = "aeiou"
str2 = "AEIOU"
str3 = ","
remove_translation = str.maketrans(str1, str2, str3)
text_with_spaces = "hello,world"
result_with_removal = text_with_spaces.translate(remove_translation)
print(f"\n原文本: '{text_with_spaces}'")
print(f"映射规则: 小写元音->大写元音, 删除,")
print(f"翻译后: '{result_with_removal}'")





