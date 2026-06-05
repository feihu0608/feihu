# | **os.rename(old,new)** | 重命名文件或者文件夹               |
import os
import shutil

# os.rename("./content","./mylove")
# | ---------------------- | ------------------------ |
# | **os.remove(file)**    | 删除文件不能删除文件夹                |
# os.remove("./mylove") #不能删除文件夹
# os.remove("./mylove/test.txt")



# | **os.mkdir(dir)**      | 创建目录，不支持递归创建,多层文件夹 |

# if not os.path.exists("./mylove1"):
#     os.mkdir("./mylove1") #只能创建单层目录
# os.mkdir('./a/b/c')  #不能一次性创建多层目录

if not os.path.exists("./a/b/c"):
# # | **os.makedirs(dir)**   | 递归创建目录             |
    os.makedirs("./a/b/c")



# | **os.getcwd()**        | 获取当前路径,获取当前文件的绝对路径             |
# print(os.getcwd())




# | **os.chdir(dir)**      | 进入指定目录             |
# os.chdir("a/b/c")
# print(os.getcwd())




# | **os.listdir(dir)**    | 获取目录下文件和目录列表 |
# print(os.listdir(r"D:\我的图片"))



# | **os.rmdir(dir)**      | 删除空目录               |

# os.rmdir("mylove1")
# os.rmdir("mylove") # 不能删除有东西的目录

# | **os.removedirs(dir)** | 递归删除空目录           |
# os.removedirs("a/b/c") # 不能直接写a 因为bc算a的内容


# 删除有内容的目录 无论单层还是多层.用到时候眼睛擦亮
# shutil.rmtree("aa")
# shutil.rmtree("a")


# os.path.dirname(path)  获取路径的目录部分
# print(os.path.dirname(r"D:/我的图片/mylove07.jpg"))

# os.path.join(*paths)
# print(os.path.join(r"D:/我的图片", "zhaoliying")) 拼接多个路径在一起

# **os.path.split(path)**  分隔路径为路径和文件名的元组
# print(os.path.split(r"D:/我的图片/mylove07.jpg"))
# **os.path.splitext(path)** 把路径分隔成文件名和扩展名的元组
# print(os.path.splitext(r"D:/我的图片/mylove07.jpg"))

# os.path.isfile(path) 判断给的路径是不是文件
print(os.path.isfile("mylove/mylove.png"))
# os.path.isdir(path) 判断给的路径是不是文件夹
print(os.path.isdir("mylove/mylove.png"))



# os.path.getsize(path) 计算文件的大小
print(os.path.getsize("mylove/mylove.png"))
print(os.path.getsize("mylove")) #拿目录的大小都是0 如果要拿自己遍历 递归


