#ポリモフィズム(多態性)
from abc import abstractmethod, ABCMeta

class Human(metaclass=ABCMeta):#親クラス

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def say_something(self):
        pass


    def say_name(self):
        print(self.name)

class Woman(Human):

    def say_something(self):
        print('女性:  名前は={}'.format(self.name))

class Man(Human):

    def say_something(self):
        print('男性:  名前は={}'.format(self.name))


#
num = input('0か1を入力してください')
if num == '0':
    human = Man('Toro')
elif num == '1':
    human = Woman('Hnako')
else:
    print('入力が間違っています')
human.say_something()

# human = Woman('Hanako')



