# 小文件的复制
# readf = open(r"C:\Users\Administrator\Desktop\0331大模型python基础.txt",'r',encoding='utf-8')
# writef = open(r"./content/课程笔记.txt",'w',encoding='utf-8')
#
# content = readf.read()
# writef.write(content)
#
# readf.close()
# writef.close()


# 大文件的复制
import shutil
# shutil.copy2("读取的文件路径（源头）","写入的文件路径（目标）")
# shutil.copy2(r"D:/我的图片/mylove04.png",r"./content/mylove.png")

# 这个比上面写效率更好，因为我们可以自己把切块切的大点，默认底层是 8192 字节
# shutil.copyfileobj(open(r"D:/我的图片/mylove05.png", "rb"), open(r"./content/mylove1.png","wb"), 1024*1024)



# 复制目录（文件夹）
shutil.copytree(r"D:\我的图片","./content/images")

