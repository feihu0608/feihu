# 并集        a|b        a和b所有的元素去重后
# 交集        a&b		   a和b都有的元素
# 差集        a-b        a中有但是b中没有的元素
# 对称差集    a^b       （a并b） - （a交b）
# 子集超集    a >= b     b的元素包含在a中， a就是b的超集，b就是a的子集



set1 = {4,5}
set2 = {4,5,6,7,8}
print(set1 | set2) #并集
print(set1 & set2) #交集
print(set2 - set1) #差集  set2当中有的但是set1当中没有
print(set1 ^ set2) #对称差集  set1并上set2 减去 set1交上set2
print(set1 > set2)  #看set2的所有元素是不是都在set1当中，是set1就是set2的超集 set2就是set1的子集


# 方法（了解）
# print(set1.union(set2)) #并      |

# 交 &
# print(set1.intersection(set2))  #不改变原集合
# print(set1.intersection_update(set2)) #把原集合改为最终的结果
# print(set1,set2)

# 差集 -
# print(set1.difference(set2))  #set1当中有的set2没有
# print(set2.difference(set1))  #set2当中有的set1没有
# set1.difference_update(set2) #set1原集合改为求出来的差集集合
# print(set1,set2)

# 对称差集
# print(set1.symmetric_difference(set2))  #set1并上set2 减去  set1交上set2
# print(set2.symmetric_difference(set1))  #set2并上set1 减去  set2交上set1
# set1.symmetric_difference_update(set2) #set1原集合改为求出来的对称差集集合
# print(set1,set2)

# 超集子集

#
# print(set1.issuperset(set2))
# print(set2.issuperset(set1))
# print(set1.issubset(set2))
# print(set2.issubset(set1))



# 坑：
#  如果采用运算符去运算 那么参与运算的都得是集合
#  如果采用方法去运算，那么调用方法的对象必须是集合，参数可以是其他的可迭代对象















