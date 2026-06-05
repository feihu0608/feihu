class Person:
    num = 10
    def __init__(self,name,age):
        self.name=name
        self.age=age

    @classmethod
    def class_method(cls):
        print(cls.num)
        print("类方法")

    @staticmethod
    def static_method():
        print("静态方法")

class Student(Person):

    num = 100

    def __init__(self,name,age):
        super().__init__(name,age)

#     重写类方法
    @classmethod
    def class_method(cls):

        # 调用父类的类方法

        # super().class_method() #super(代表父类)，调用类方法的时候，cls传递的是子类
        Person.class_method() #cls默认传递父类
        print("类方法1")


    @staticmethod
    def static_method():
        # 调用父类的静态方法
        # 以后不要用super()直接调用静态方法
        # super() == = > super(本类，cls / self)，而静态方法当中没有cls / self
        # super().static_method()
        # super(Student,Student).static_method()

        Person.static_method()
        print("静态方法1")


# 类方法是无条件继承法 自己 有就调自己的 没有就找爹
# 坑
# 重写父类方法，在子类的类方法当中调用父类的类方法（super和父类名去调用的时候默认给cls传递的参数不一样）
Student.class_method()


# 静态方法也是无条件继承，自己有就调自己的，没有就找爹
# 坑
# cls代表在类方法调用，默认拿类方法的第一个参数cls传递
# self代表在实例方法调用，默认就拿实例方法的第一个参数self传递
# 静态方法没有cls/self 所以默认直接调用就炸
# super() ==>  super(当前执行的类，cls/self)

Student.static_method()

