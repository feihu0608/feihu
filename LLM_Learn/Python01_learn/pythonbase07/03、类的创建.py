class Car(object):
    """
        class的作用后期可以创建车的实例
    """


    # object 基类
#     类体(当中写的属性方法都叫这个类的成员)

    num = 100 #类属性

    # 实例方法（类的一个成员）
    def __init__(self, name, price, brand,color):
        self.name = name
        self.price = price
        self.brand = brand
        self.color = color

    def run(self):
        print(f"{self.name}车跑了")


    @classmethod
    def class_method(cls):
        print("类方法")

    @staticmethod
    def static_method():
        print("静态方法")

# 1、对类的实例化 目的就是为了创建这个类的对象
c = Car("幻影",10000000,'劳斯莱斯','black')
# c.run()
# print(c.name)
# print(c.price)
# print(c.brand)
# print(c.color)


Car.run(c)
# 后期类里面定义的实例方法有两种调用方式
# 1、实例化对象 对象.方法（）去调用
# 2、类的成员类可以直接访问  类.方法（实例化对象）
# 类里面形参第一个是self的方法被称作叫实例方法，必须有实例化对象的参与才能调用



# 2、对类的成员进行引用(引用方法的时候我们不要加括号，加了括号叫方法调用)
print(Car.__doc__)
print(Car.num)
print(Car.__init__)
print(Car.run)
print(Car.class_method)
print(Car.static_method)







