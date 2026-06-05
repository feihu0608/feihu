# 定义父类
class A:
    def show_one(self):
        print("A的show_one")
    def show_two(self):
        print("A的show_two")
    def show_three(self):
        print("A的show_three")
    def show_four(self):
        print("A的show_four")

# 定义父类
class B(A):
    def show_one(self):
        print("B")
    def show_two(self):
        print("B的show_two")
    def show_three(self):
        print("B的show_three")
        super().show_three()
    def show_four(self):
        print("B的show_four")
        super().show_four()

# 定义父类
class C(A):
    def show_one(self):
        print("C的show_one")
    def show_two(self):
        print("C的show_two")
    def show_three(self):
        print("C的show_three")
    def show_four(self):
        print("C的show_four")
        super().show_four()


# 定义子类
class D(B,C):
    def show_one(self):
        print("D的show_one")
    def show_two(self):
        print("D的show_two")
        super().show_two()
    def show_three(self):
        print("D的show_three")
        super().show_three()
    def show_four(self):
        print("D的show_four")
        super().show_four()


# mro的顺序是从哪个类的实例开始调用的时候就确定死了
# super()在找父类的时候，就是严格按照这个mro顺序去查找
# 找完了D找B，找完B找C,最后找A


# 我们没有从D开始，而是从B开始
# 找完B 找A




# print(D.mro())
# d = D()
# d.show_one()
# d.show_two()
# d.show_three()
# d.show_four()


b = B()
print(B.mro())
b.show_one()
b.show_two()
b.show_three()




