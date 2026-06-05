# 初始化代码 指定在默认import这个包的时候，我们默认引入哪些模块

from . import basic_arithmetic
# 在直接import包的时候，默认引入的是basic_arithmetic  要用包.basic_arithmetic

__all__ = ['advance_calculate']
# from 包 import *  作用是限定*的范围 后期用的时候 可以直接写范围内的模块，没有在范围内不能写
