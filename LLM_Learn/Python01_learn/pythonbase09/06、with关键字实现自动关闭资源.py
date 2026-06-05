f = None
try:
    a = 100
    print(a)
    f = open("./mylove/mylove.png", "rb")
    # with open("./mylove/mylove.png", "rb") as f:
    #     pass
    b = 200
    print(b)
    # f.close()
    print(f.closed)

except Exception as e:
    print(e)
finally:
    f.close()  #以后如果不用with，关闭资源最好在这里，不要在try当中关闭
#              如果放在try当中，打开文件和关闭文件中间一旦有异常，文件就关不了
