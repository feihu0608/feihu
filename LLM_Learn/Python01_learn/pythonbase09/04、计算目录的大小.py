import os
# os.walk传递一个目录的话，它会自动做递归，返回的是1根路径  2当前目录当中的目录列表  3、当前目录当中的文件列表组成的元组
# os.walk()




# result = os.walk(r"C:\Users\Administrator\Desktop\0331pythonbase")
# print(result)
# for item in result:
#     print(item)

# total_size = 0
# for root,dirs,files in os.walk(r"C:\Users\Administrator\Desktop\0331pythonbase"):
#     for file in files:
#         filepath = os.path.join(root,file)
#         if not os.path.islink(filepath):
#             total_size += os.path.getsize(filepath)
# print(total_size/1024/1024)


# print(sum([
#     os.path.getsize(os.path.join(root, file))
#     for root, dirs, files in os.walk(r"C:\Users\Administrator\Desktop\0331pythonbase")
#     for file in files if not os.path.islink(os.path.join(root, file))
# ])/1024/1024)


def get_dir_size(path):
    return sum([
        os.path.getsize(os.path.join(root, file))
        for root, dirs, files in os.walk(path)
        for file in files if not os.path.islink(os.path.join(root, file))
    ]) / 1024 / 1024


size = get_dir_size(r"C:\Users\Administrator\Desktop\0331pythonbase")
print(size)



# list1 = [1,2,3]
# print(list1[6])