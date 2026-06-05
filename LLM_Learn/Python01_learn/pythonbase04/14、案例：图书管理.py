# 1、一上来先让客户看到一行欢迎语
# 2、客户可以选择功能:1、添加图书  2、根据id修改图书  3、根据id查询单个图书 4、查询所有图书 5、根据id删除某个图书 6、退出
# 3、客户没有退出，完成功能后，可以继续从新选择功能（死循环）

book_list = [] #管理图书

print("*"*30 + "欢迎来到图书管理系统" + "*" * 30) #显示欢迎语

while True:
    num = int(input("请输入您的操作编号：1、添加图书  2、根据id修改图书 "
                    " 3、根据id查询单个图书 4、查询所有图书 5、根据id删除某个图书 6、退出"))
    match num:
        case 1:
            book_id = int(input("请输入书的编号id"))
            book_name = input("请输入要添加的书名")
            book_author = input('请输入书的作者')
            book_price = float(input("请输入书的价格"))
            book_dict = {"book_name": book_name, "book_author": book_author,"book_price": book_price, "book_id": book_id}
            book_list.append(book_dict)
            print("添加成功")
        case 2:
            book_id = int(input("请输入您要修改的书编号id"))
        #     遍历列表
            for book in book_list:
                if book["book_id"] == book_id:
        #             存在，改
                    book_name = input("请输入要修改的书名")
                    book_author = input('请输入修改的书的作者')
                    book_price = float(input("请输入修改的书的价格"))

                    book.update({
                        "book_name": book_name,
                        "book_author": book_author,
                        "book_price": book_price,
                    })
                    print("修改成功")
                    break
            else:
                print("输入的书不存在")


        case 3:
            book_id = int(input("请输入您要查询的书编号id"))
            for book in book_list:
                if book["book_id"] == book_id:
                    print(f"找到了这个书，书的信息{book['book_name']} --- {book['book_price']} --- {book['book_author']}")
                    break
            else:
                print("没找到你输入的书")

        case 4:
            if book_list:  #所有的空容器默认为False,容器里面有东西就是True
                for book in book_list:
                    print(f"书的信息{book['book_name']} --- {book['book_price']} --- {book['book_author']}")
            else:
                print("目前没有书籍")
        case 5:
            book_id = int(input("请输入您要查询的书编号id"))
            for i,book in enumerate(book_list):
                if book["book_id"] == book_id:
                    del book_list[i]
                    print("删除成功")
                    break
            else:
                print("没有找到你要删除的书")


        case 6:
            print("欢迎下次光临")
            break
        case _:
            print("您的输入有误，必须是1 - 6")












