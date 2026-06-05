# import sys
# print(sys.path)


# 一、、import 模块 [as 别名] 默认把模块当中所有的非私有的数据，全部导入
# import mymath
# import myshape as ms
#
# print(mymath.list1)
# print(mymath.add(10, 20))
# print(mymath._remainder(10, 20))
# # 通过模块.xxx获取所有的非私有数据干活
#
# # 模块引入的时候取别名操作
# ms.print_rectangle(10, 30)


# 二、from 模块 import 要用的数据1,要用的数据2
# from mymath import add as ad,subtract as sub,multiply as mul
# from myshape import multiply
# # 坑：不同模块里面有相同的数据，此时我们通过分别引入的方式引入数据的时候，一定要取别名，否则后引入的会覆盖前面的
#
# print(ad(10, 20))
# print(sub(10,20))
#
# multiply(10, 20)
# print(mul(10, 20))



# 三、from模块import *
# from mymath import *
# # 1、*代表通配符，默认代表所有的非私有数据，而且不能强制访问
# add(10, 20)
# multiply(10, 20)
# subtract(10, 20)
# divide(10,20)
# _remainder() 默认不能强制访问，但是可以修改__all__设置让外部强制访问


# 2、通配符默认的场景（引入所有非私有）我们是可以手动改变的
# 在模块当中有一个特殊的列表可以设置   __all__



#引入一下mymath,什么都不做
# import mymath
from mymath import add
print(__name__)

# 1、任何的模块都是.py文件，那么只要是.py文件就有两种运行方式（1、作为主文件运行，2、作为模块导入运行）
# 2、任何.py文件当中都有__name__,这个变量打印的时候根据当前.py文件是如何执行的，结果不一样
#     2-1：如果当前这个文件是作为主文件运行的，我们自己右击run起来，那么__name__结果是__main__固定的
#     2-2：如果当前这个文件是作为模块引入运行的，此时__name__ = 包.模块名


# 后期我们在写主文件代码的时候，下面是标配
# if __name__ == '__main__':
#     pass









