# 字符串intern机制，如果内存当中已经有了这个字符串，后期如果还要存储相同的字符串，那么内存当中只有一份

str1 = "zhaoliying"
print(str1,id(str1))

str2 = "zhaoliying"
print(str2,id(str2))
