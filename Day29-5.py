#インスタンスメソッド、クラスメソッド、スタティクメソッド
class Human:

    class_name = 'Human' #クラス変数

    def __init__(self, age, name): #コンストラクト
        self.name = name
        self.age =age

    def print_name_age(self): #インスタンスメソッド
        print('インスタンスメソッド実行')
        print('name = {} age = {}'.format(self.name, self.age))

    @classmethod #クラスメソッド
    def print_class_name(cls , msg):
        print('クラスメソッド実行')
        print(cls.class_name) #クラス変数
        print(msg)

    @staticmethod #スタティクメソッド
    def print_msg(msg):
        print('スタティックメソッド実行')
        print(msg)

Human.print_class_name('こんにちは')
man = Human('桜木',18)
man.print_name_age()
man.print_msg('hello static')
Human.print_msg('hello static')

