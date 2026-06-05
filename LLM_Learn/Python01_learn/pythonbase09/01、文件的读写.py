
# 文件的写
# # 1、打开文件
# f = open(r"D:/aaa/test.txt","w")
# # 2、执行操作
# # f.write("我爱你刘诗诗\n")
# # f.write("我爱你杨幂")
#
#
# content_list = ["我爱你刘诗诗\n","我爱你杨幂\n","我爱你赵丽颖"]
#
# f.writelines(content_list)
# # 3、关闭文件
# f.close()


# 文件的读
f = open("./content/test.txt","r",encoding="utf-8")
# print(f.read())
# print(f.read(10))

# print(f.readline())
# print(f.readline(10))


# print(f.readlines())
# print(f.readlines(100))

f.close()