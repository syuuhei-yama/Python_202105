#関数　基礎
# def hello():
#     print("hello world")
#
# hello()
#
# def num_max(a, b):
#     print("a = {}, b = {}".format(a, b))
#     if a > b:
#          return a
#     else:
#         return b
#
# print(num_max(b = 10,  a = 20))
# print(num_max(10, 100))

#関数　応用
def sample(arg1, arg2 = 100):
    print(arg1, arg2)

sample(200)

def spem(arg1, *arg2):
    print("arg1={}, arg2={}".format(arg1,arg2))
    print(type(arg2))

spem(1,2,3,4,5)


def spem2(arg1, **arg2):
    print("arg1={}, arg2={}".format(arg1, arg2))
    print(type(arg2))

spem2(3, name="yama",age=25)


def spem3(arg1, *arg2, **arg3):
    print(arg1, arg2, arg3)

spem3(1, 2, 3, 4, 5,name="yama",age=25)


def sample_2():
    return 1, 2, 3

a, b, c = sample_2()
print(a, b, c)

