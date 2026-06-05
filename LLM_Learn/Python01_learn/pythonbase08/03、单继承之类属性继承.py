class Person:
    num = 1
    _num = 2
    __num = 3 #_Person__num
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    num = 100
    _num = 200
    __num = 300  #_Student__num


    def __init__(self, name, age, score):
        super().__init__(name, age)
        self.score = score


print(Student.num)
print(Student._num)
print(Student._Person__num)
print(Student._Student__num)

# 类属性继承（无条件继承）
# 类属性会继承父类的所有，如果子类没有同名属性，可以直接访问父类的
# 如果子类有父类的同名属性，那么就访问子类的自己的
# 子类和父类双下滑线私有类属性，都可以通过改名的方式让子类获取到，但是不建议
#
# 注意：通过改名的方式去获取私有属性，本来就是不建议的，虽然可以拿到，谁的私有属性就在哪个类定义接口才是正解