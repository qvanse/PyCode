import random as r
class aaa:
    def __init__(self,name):
        self.name=name
    
    def Hi(self):
        print('Hi! %s ,Hello!' % self.name)

# h=Hello('lily')
# h.Hi()

class bbb:
    def p(self):
        print("这个是父类方法！")

class ccc(bbb):
    def p(self):
        print('这个是子类方法！')

class Fish:
    def __init__(self):
        self.x=r.randint(1,10)
        self.y=r.randint(1,10)
    def move(self):
        self.x-=1
        # print('位置是：' self.x,self.y)   
        print('位置：',self.x,self.y)

class GoldFish(Fish):
    pass
class Crap(Fish):
    pass
class Salmon(Fish):
    pass
class Shark(Fish):
    def __init__(self):
        super().__init__()
        self.hungry=True
    def eat(self):
        if self.hungry:
            
            print("吃货天天开心")
            self.hungry=False
        else:
            print("吃饱了")
            
class Base1:
    def foo1(self):
        print("我是Base1-->foo1")

class Base2:
    def foo2(self):
        print("我是Base2-->foo2")

class Base3:
    def foo3(self):
        print("我是Base3-->foo3")

class Base0(Base1,Base2,Base3):
    pass

        
 








if __name__ == "__main__":
    h=aaa('Lily')
    h.Hi()
    p=bbb()
    p.p()

