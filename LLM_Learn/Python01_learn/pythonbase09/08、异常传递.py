try:
    print("嘿嘿")
    try:
        print("哈哈")
        # result = 10 / 0
        # print(result)
        try:
            a = 100
            print(a)
            f = open("xxxxx","r")
            b = 200
            print(b)
        except ValueError as e:
            print(e)
    except ZeroDivisionError as e:
        print(e)
except IndexError as e:
    print(e)