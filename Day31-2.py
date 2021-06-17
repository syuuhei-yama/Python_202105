#プライベート変数　外部からアクセス出来ない変数（厳密にはPythonではアクセス可能、java等は絶対不可）
# class Human:
#     __class_val = 'Human'
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def print_msg(self):
#         print('name = {}, age = {}'.format(self.__name, self.__age))
#
#
# human = Human('Toro',15)
# human.print_msg()


#カプセル化(基礎) -> クラス外部から変数が見えないようにすること。getter・setterを使用する。　変数　= property(get_変数名, set_変数名)
# class Human:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def get_name(self):
#         print('getter name　を呼び出しました')
#         return self.__name
#
#     def get_age(self):
#         print('getter age を呼び出しました')
#         return self.__age
#
#     def set_name(self, name):
#         print('setter name を呼び出しました')
#         self.__name = name
#
#     def set_age(self, age):
#         print('setter age を呼び出しました')
#         self.__age = age
#
#     name = property(get_name,set_name)
#     age = property(get_age,set_age)
#
#     def print_msg(self):
#         print(self.name,self.age)
#
# human = Human('Toro', 15)
# human.name = 'Jiro'
# human.age = 19
#
# name = human.name
# age = human.age
# print(name, age)
# human.print_msg()

#　応用
class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self): # getter
        print('getter nameが呼ばれました')
        return self.__name

    @property
    def age(self):
        print('getter ageが呼ばれました')
        return self.__age

    @name.setter
    def name(self, name):
        print('setter が呼ばれました')
        self.__name = name

    @age.setter
    def age(self, age):
        print('setter ageが呼ばれました')
        if age < 0:
            print('0以上の値を設定してください')
            return
        self.__age = age

human = Human('Kouichi', 22)
human.name = 'yama'
print(human.name)
human.age = -1
print(human.age)

