import types


def eat1(self):
    print(f"{self.name}吃饭")


@classmethod
def class_method(cls):
    print("类方法用了")

@staticmethod
def static_method():
    print("静态方法用了")

a = 200

class Student:

    num = a #动态添加类属性

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def study(self):
        print(f"{self.name}在学习")

    eat = eat1 #动态添加了实例方法

    class_method = class_method #动态添加了类方法

    static_method = static_method #动态添加了静态方法


s1 = Student("张三",18,"male")
print(s1.name)
print(s1.age)
print(s1.gender)
s1.study()







# 动态给类添加方法（类方法 静态方法 实例方法,类属性）
# 1、可以在类里面直接写变量，在类外面定义相应的方法或者变量（类shuxing）
s1.eat() #添加实例方法
Student.eat(s1)
Student.class_method()
Student.static_method()
print(Student.num)

# 2、不需要在类里面写变量，而是直接通过类.新的名字 = 方法或者属性值

# 给类里面添加了一个实例方法，但是这个实例方法是后期所有的实例化对象都能调
def sleep(self):
    print(f"{self.name}在睡觉")
Student.sleep = sleep

@classmethod
def class_method1(cls):
    print("类方法1调用了")
Student.class_method1 = class_method1

@staticmethod
def static_method1():
    print("静态方法1调用了")
Student.static_method1 = static_method1

s1.sleep()
Student.class_method1()
Student.static_method1()
Student.num2 = 20000
print(Student.num)
print(Student.num2)


# 动态给实例添加属性和方法（是给当前这个实例自己对象身上添加的属性和方法，其它的实例没有）
s2 = Student("李四",18,"male")
print(s2.name)
print(s2.age)
print(s2.gender)


# 动态添加一个实例属性
s2.height = 1.70
print(s2.height)
# print(s1.height) #炸它没有给自己添加


# 动态给实例添加实例方法，但是这样添加无法使用self,那么方法当中无法使用当前对象的属性
# def play():
#     print("学生玩耍")
# s2.play = play



# 动态给实例添加实例方法，但是这样添加可以使用self
def play(self):
    print(f"{self.name}学生玩耍")
s2.play = types.MethodType(play,s2)
s2.play()
# s1.play()






















