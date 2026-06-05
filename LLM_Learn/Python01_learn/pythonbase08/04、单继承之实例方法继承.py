from time import sleep


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print("人吃饭")

    def __sleep(self):
        # 私有方法
        print("sleep")

    def get_sleep(self):
        self.__sleep()


class Student(Person):
    def __init__(self,name,age):
        super().__init__(name,age)

    # 方法重写  重写父类的同名方法
    def eat(self):
        print("学生吃肉")

    def __sleep(self):
        print("学生睡觉")


s = Student("zhangsan",19)
s.eat()  # ==> Person.eat(s)


s._Person__sleep()  #这样不建议