class Dog(object):

    num = 100  #类属性


    def __init__(self,name,age,color):
        # init当中缩写的这些self.xxx就叫实例属性
        self.name = name
        self.age = age
        self.color = color


    # 打印对象整体的时候自动调用
    def __str__(self):
        return f"""
            名字：{self.name},
            年龄：{self.age},
            颜色：{self.color}
        """

    # 删除一个实例对象的时候自动调用
    def __del__(self):
        print(f"对象{self.name}删除了")


    # 第一个形参是self我们把他们称作是实例方法
    def eat(self):
        print("狗吃骨头")

    def sleep(self):
        print("狗在sleep")

    def bark(self):
        print("狗在叫")

    def bark_and_run(self):
        self.bark()
        print("狗跑")

    @classmethod
    def class_method(cls):
#         类方法
        print("这个是类方法")
#         类方法里面可以访问类的属性 因为它有cls,就算没有也可以通过Dog直接访问
        print(cls.num)
        print(Dog.num)
#         类方法当中没办法获取self,所以实例身上的属性无法获取

    @staticmethod
    def static_method():
#         静态方法
        print("这个是静态方法")
#         虽然它没有cls，但是可以直接拿Dog类型去访问类属性

        print(Dog.num)
#         静态方法和类方法很像，都无法获取访问实例属性








#一、 实例属性
# 1、可以通过实例化对象访问实例身上的属性
d1 = Dog("旺财",2,"yellow")
d1.name = "大黄"
print(d1.name)
print(d1.age)
print(d1.color)

# 2、通过类访问实例属性是不能访问的
# print(Dog.name)

# 实例的属性只有实例才能访问，类是无法访问实例属性的




#二、 实例方法
# 1、实例方法本意就是给实例去调用的，所以实例调用实例方法天经地义
d1.eat()
d1.sleep()
d1.bark()
d1.bark_and_run()

# 2、类调用实例方法
Dog.eat(d1)

# 实例方法，实例可以调用，类也可以调用，只是类在调用的时候需要手动传递实例


#三、类属性
# 1、类去访问这个类属性,天经地义 类属性本意就是让类去访问的
print(Dog.num)
# 2、实例去访问类属性,实例访问也可以直接访问类属性
print(d1.num)

# 注意修改的时候：
# 通过类去修改类属性
Dog.num = 1000
print(Dog.num)
print(d1.num)

# 通过实例去修改类属性(本质不是在修改类的属性，而是给这个实例添加了一个新属性叫num)
d1.num = 2000
print(Dog.num)
print(d1.num)

# 最佳实践：以后记住谁的属性就谁去访问和修改


# 四、类方法的使用和注意事项
# 1、类调用类方法,天经地义
Dog.class_method()
# 2、实例调用类方法
d1.class_method()
# 类方法类和实例都可以调用
# 但是类方法当中想要获取实例的属性是不可能的，但是可以通过两种方式获取类的属性（cls,类名.属性）



# 五、静态方法的使用和注意事项
Dog.static_method()
d1.static_method()
# 类和实例都可以调用，静态方法内部也是访问不了实例属性，但是可以访问类属性（只能通过类名.属性）



# 六、魔术方法
print(d1)

# 删除一个实例对象
# del d1
d1 = None


# print(d1)


# 区别：
# 他们都可以完成相同的功能，后期我们使用类方法和静态方法主要就是为了做工具类
# 类方法一般都是和这个类有关联的方法，一般就认为类方法当中要访问这个类相关的属性
# 最佳实现，区别没那么明显，后期你也可以使用类方法去封装工具类

class Calculate(object):
    @classmethod
    def add(cls,a,b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b


print(Calculate.add(1, 2))







































