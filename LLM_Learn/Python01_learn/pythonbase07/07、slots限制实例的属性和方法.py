import types


class Teacher(object):
    # 限定实例身上的属性和方法有哪些范围，一旦限定了这些词汇，类当中不能使用这些词汇
    __slots__ = ("name","age","gender","eat")

    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        # self.id = id

    # 'eat' in __slots__ conflicts with class variable 类变量使用slots限定的词汇
    # def eat(self):
    #     print("eat")


t1 = Teacher("John",23,"male")
print(t1.name)
print(t1.age)
print(t1.gender)
# print(t1.id)
def eat(self):
    print("eat")
t1.eat = types.MethodType(eat,t1)
t1.eat()


def sleep(self):
    print("sleep")
t1.sleep = types.MethodType(sleep,t1)
t1.sleep()
