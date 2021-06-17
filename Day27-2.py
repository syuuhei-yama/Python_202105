#高階関数

# def print_hellow():
#     print("hello")
#
# def print_goodbyee():
#     print("goodbyee")
#
# var = ["AA","BB",print_hellow,print_goodbyee]
# var[2]()
# var[3]()


def print_world(msg):
    print("{} world".format(msg))

def print_konnitiwa():
    print("こんにちは")

def print_hellow(func):
    func("hellow")
    return print_konnitiwa()

var = print_hellow(print_world)
var()