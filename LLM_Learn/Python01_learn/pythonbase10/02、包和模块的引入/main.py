# 导入包的方式
# 1、import mymath  直接引入包
import mymath
print(mymath.basic_arithmetic.add(10, 20))


# 2、引入包当中模块
# import mygraphic.circle
# print(mygraphic.circle.area(5))

from mygraphic import rectangle

print(rectangle.area(3, 4))


# 3、引入模块当中的成员数据
from mymath.advance_calculate import my_power
print(my_power(2,3))



# 4 从包引入* 所有
from mymath import *
advance_calculate.my_power(2, 3)  #针对*的范围，需要在init当中限定__all__
mymath.basic_arithmetic.add(10, 20)  #针对直接引入包 需要在init当中写初始化代码




# 最佳实践
# 以后不要直接import包
# 以后我们最好从包导模块,然后通过模块去拿数据
# 如果你确定知道这是一个模块，那么就import模块 还是通过模块.xxx去找数据









