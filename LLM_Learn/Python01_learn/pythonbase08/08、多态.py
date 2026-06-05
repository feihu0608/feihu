# # 基于继承的多态
# class Animal(object):
#     def bark(self):
#         print("动物在叫")
#
# class Dog(Animal):
#     def bark(self):
#         print("汪汪叫")
#
# class Cat(Animal):
#     def bark(self):
#         print("喵喵叫")
#
# class Bird(Animal):
#     def bark(self):
#         print("咕咕叫")
#
# # 这个函数传递不同的对象，最终表现的形式（叫声）不一样，这个就是多态
# def print_bark(obj):
#     obj.bark()
#
# d = Dog()
# c = Cat()
# b = Bird()
# print_bark(d)
# print_bark(c)
# print_bark(b)



# 鸭子类型（动态类型）

class Dog:
    def bark(self):
        print("汪汪叫")

class Car:
    def bark(self):
        print("滴滴叫")

class Phone:
    def bark(self):
        print("铃铃叫")

def print_bark(obj):
    obj.bark()

dog = Dog()
car = Car()
phone = Phone()
print_bark(dog)
print_bark(car)
print_bark(phone)



