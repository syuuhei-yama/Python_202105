#クラスの定義
# class Car:
#     country = "japan"
#     year = 2019
#     name = "prius"
#     def print_name(self):
#         print('print_self実行')
#         print(self.name)
#
# my_car = Car()
# print(my_car.year)
# my_car.print_name()
# list_a = ['apple','banana',Car()]
# # second_car = list_a[2]()
# # second_car.print_name()
# list_a[2].print_name()
# help(Car)


#クラス変数,インスタンス変数

# class sampleA():
#     class_val = 'class val' #クラス変数
#
#     def set_val(self):
#         self.instance_val = 'instance val' #インスタンス変数
#
#     def print_val(self):
#         print('クラス変数 = {}'.format(self.class_val))
#         print('インスタンス変数 = {}'.format(self.instance_val))
#
# isinstance_a = sampleA() #インスタンス化
# isinstance_a.set_val()
# print(isinstance_a.instance_val)
# isinstance_a.print_val()
# print(sampleA.class_val)
# print(isinstance_a.__class__.class_val)
# isinstance_b = sampleA()
# isinstance_b.set_val()
# isinstance_b.print_val()
# isinstance_a.__class__.class_val = 'class val 2'
# isinstance_b.print_val()
#
# print(id(isinstance_a.__class__.class_val))
# print(id(isinstance_b.__class__.class_val))


#コンストラクター, デストラクター
class SampleClass:
    def __init__(self, msg, name=None):#コンストラクター
        print('コンストラクターが呼ばれました')
        self.msg = msg
        self.name = name

    def __del__(self):
        print('デストラクターが実行されました')
        print('name = {}'.format(self.name))

    def print_msg(self):
        print(self.msg)

    def print_name(self):
        print(self.name)

var1 = SampleClass('Hello' , 'jiro')
var1.print_msg()
var1.print_name()
del var1


