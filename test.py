class Turtle:
    color='green'
    def run(self):
        print("努力的奔跑!")


class Bill:
    def __init__(self,name):
        self.name=name

    def kick(self):
        print('我是%s,谁在路踢我？' % self.name)

class person:
    __name='小甲鱼'
    def getName(self):
        return self.__name


if __name__ == "__main__":
    tt=Turtle()
    tt.run()
    print(tt.color)