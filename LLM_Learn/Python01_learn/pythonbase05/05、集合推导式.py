set1 = {1,2,3,4}
set2 = set()
for item in set1:
    set2.add(item)
print(set2,set1,id(set2),id(set1))

# 集合推导式
set3 = {item for item in set1 if item  % 2 == 0}
print(set1,set3)