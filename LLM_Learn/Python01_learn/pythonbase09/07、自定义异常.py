from exceptions.customexception import CustomException


def checkout():
    # 支付的业务逻辑
    count = 5
    store = 3

    if count > store:
#         要抛出一个异常，抛出了异常，才能try
#         raise #专门用来在我们业务出现问题的时候去抛异常，然后才能捕获去处理
#         raise最终其实就是抛了一个异常对象
#         raise ValueError("购买的商品库存不足")
        raise CustomException("购买的商品库存不足")
try:
    checkout()
# except ValueError as e:
#     print(e)
    # print("用户购买商品库存不足，等待补货")
except CustomException as e:
    print(e)
    # print("用户购买商品库存不足，等待补货")



# ValueError是系统异常，所有的系统异常类，都可以让我们自己手动实例化对象往外抛
# 吐过我们业务的异常使用系统异常类去抛出，会有歧义，此时我们应该自己造一个异常（自定义异常类）