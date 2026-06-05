class Person(object):
    def __init__(self, name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.hp = 100

#   后期我们设计的类，一定是通过某个方法关联到一起
    def fire(self,gun,person):
        print(f"{self.name}开抢了，枪是一个{gun.name}")
        gun.shoot(person)

class Gun(object):
    def __init__(self,name):
        self.name = name

    def shoot(self,person):
        person.hp -= 30
        if person.hp <= 0:
            person.hp = 0
            print(f"{person.name}被打死了")
        else:
            print(f"{person.name}的血量还有{person.hp}")



if __name__ == '__main__':
    laowang = Person("老王",50,"male")
    laozhang = Person("老张",58,"male")
    gun = Gun("加特林")

    while laozhang.hp > 0:
        laowang.fire(gun,laozhang)
    laozhang = None







