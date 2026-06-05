class Person:
    def __init__(self,name,age):
        self.name=name
        self._age=age
        self.__money=100

class Student(Person):
    # pass
    def __init__(self,name,age):
        # self.name = name
        # self._age = age
        super().__init__(name,age)
        # 我们本意是想把上面name和age赋值通过调用父类的init做个简化，但是
        # 此时父类当中有改名的私有属性，因为改名所以子类当中覆盖不了，就继承到子类实例身上
        # 我们此时就可以说有继承
        # 如果没有改名式私有属性，我们也可以说没有继承


        #手动调用父类的init，传递的self还是子类实例
        self.__money = 200
#

# 子类没有写init,默认调用的是父类的init,只要是调了父类的init，就说是实例属性做了继承
# s = Student("zhangsan",19)
# print(s.name)
# print(s._age)
# print(s._Person__money)



# 子类如果有自己的init，默认就调用自己的init,不会调用父类的init，此时实例属性不继承
# 但是如果父类实例属性有改名式私有化，我们子类实例也可以拿到父类的私有化属性，此时也可以说有继承
s2=Student("lisi",20)
print(s2.name)
print(s2._age)
print(s2._Student__money)
print(s2._Person__money)