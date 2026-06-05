class Bird(object):
    def __init__(self,name,color,attack):
        self.name = name
        self.color = color
        self.attack = attack


    def fly(self):
        print("鸟飞")

    def bark(self):
        print("鸟叫")

    def use_skill(self,obstacle):
        self.fly()
        self.bark()
        print(f"{self.name}释放了技能攻击{obstacle.name}")
        obstacle.hp -= self.attack
        if obstacle.hp <= 0:
            print(f"障碍物{obstacle.name}被摧毁")
        else:
            print(f"障碍物{obstacle.name}还有{obstacle.hp}血量")


class RedBird(Bird):
    def fly(self):
        print("很激情的飞")

    def bark(self):
        print("很激情的叫")


class YellowBird(Bird):
    def fly(self):
        print("很悲伤的飞")

    def bark(self):
        print("很悲伤的叫")


class BlueBird(Bird):
    def fly(self):
        print("很优雅的飞")

    def bark(self):
        print("很优雅的叫")


class Obstacle(object):
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp



if __name__ == "__main__":
    red = RedBird("小红","red",40)
    yellow = YellowBird("小黄","yellow",30)
    blue = BlueBird("小蓝","blue",20)

    ob1 = Obstacle("木板",100)
    ob2 = Obstacle("铁板",200)

    red.use_skill(ob1)
    yellow.use_skill(ob1)
    blue.use_skill(ob1)
    blue.use_skill(ob1)

    red.use_skill(ob2)
    yellow.use_skill(ob2)
    blue.use_skill(ob2)
    blue.use_skill(ob2)
    red.use_skill(ob2)
    yellow.use_skill(ob2)
    blue.use_skill(ob2)
    blue.use_skill(ob2)


#  其实我们在每次攻击障碍物的时候都是要去判断这个障碍物是否存在，然后决定攻击不攻击










