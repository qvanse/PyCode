import random as r
class Fish:
    def __init__(self,name):
        self.name=name
        self.x=r.randint(0,10)
        self.y=r.randint(0,10)
        print("x=%s,y=%s" %(self.x,self.y))
    def Move(self):
        self.x-=1
        print("{0}的位置是{1},{2}".format(self.name,self.x,self.y))

class GoldFish(Fish):
    pass

g=GoldFish("金鱼")
g.Move()

class Shark(Fish):
    def __init__(self,name):
        super().__init__(name)
        self.hungry=True
    def eat(self):
        if self.hungry:
            print("吃饱了！")
            self.hungry=False
        else:
            
            print("吃饭很快乐！")

s=Shark("鲨鱼")
s.Move()
s.eat()

class Turtle:
    def __init__(self,x):
        self.num=x
class Fish:
    def __init__(self,x):
        self.num=x
class Pool:
    def __init__(self,x,y):
        self.turtle=Turtle(x)
        self.fish=Fish(y)
    def getNum(self):
        print("乌龟{}只，鱼{}只".format(self.turtle.num,self.fish.num))

class CapStr(str):
    def __new__(cls,string):
        string=string.upper()
        return str.__new__(cls,string)

