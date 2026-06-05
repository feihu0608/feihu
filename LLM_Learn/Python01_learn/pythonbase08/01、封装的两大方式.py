class Person:
    def __init__(self,name,age):
        self.name=name
        # 约定式私有化 外部无法访问 加一个下划线,强制访问是警告
        self._age=age

        # 改名式私有化 外部无法访问 加两个下滑线，强制访问未改名的属性报错炸
        # 这个改名是发生在执行程序代码之前，__money在执行的时候根本不存在
        self.__money = 100  #self._Person__money=100

    # 获取年龄的接口
    def get_age(self):
        return self._age
    # 设置年龄的接口
    def set_age(self,age):
        if age>18:
            self._age=age

    # # 获取钱的接口
    # def get_money(self):
    #     return self.__money
    #
    # # 设置钱的接口
    # def set_money(self, money):
    #     if money > 0:
    #         self.__money += money

    # 通过装饰器把接口方法简化，方法可以当做属性去对待
    # 获取钱的接口（getter）
    @property
    def money(self):
        return self.__money

    # 设置钱的接口
    @money.setter #(setter)
    def money(self, money):
        if money > 0:
            self.__money += money


p = Person('yangmi',18)
print(p.name)
# print(p._age) #约定的私有化其实也可以强制访问，但是不应该这样做

# 约定式封装
print(p.get_age())
p.set_age(20)
print(p.get_age())

# 改名式封装
# print(p.__money)
# print(p._Person__money) #改名的私有化其实也可以强制访问，但是不应该这样做
# print(p.get_money())
# p.set_money(100)
# print(p.get_money())


# 接口的简化
print(p.money)
p.money = 200
print(p.money)


