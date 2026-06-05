class Fly:
    def flying(self):
        print("飞")

class Run:
    def running(self):
        print("跑")

class Swim:
    def swiming(self):
        print("游泳")



# 混入类 就是把一些技能全部单独写成类，后期哪个类要有哪个技能，只需要继承这个技能类就可以
# 可插拔
class Duck(Fly,Swim,Run):
    def __init__(self,name,age):
        self.name = name
        self.age = age


class Person(Swim,Run):
    def __init__(self,name,age):
        self.name = name
        self.age = age


print(Duck.mro())





class A:
    def func(self):
        print("A的func")

class B(A):
    def func(self):
        super().func()
        print("B的func")

class C(A):
    def func(self):
        super().func()
        print("C的func")

class D(B, C):
    pass

d = D()

C.func(d) 