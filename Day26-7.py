#ジェネレータ関数 1
# def generator(max):
#     print("ジェナレータ作成")
#     for n in range(max):
#         yield n
#         print("yield実行")
#
# gen = generator(10)
# for n in gen:
#     print("x = {}".format(n))
# n = next(gen)
# print(n)
# n = next(gen)
# print(n)

# 2

# def generator(max):
#     print("ジェナレータ作成")
#     for n in range(max):
#         try:
#             x = yield n
#             print("x = {}".format(x))
#             print("yield実行")
#         except Exception as e:
#             print("throwが発生しました")
#
# gen = generator(10)
# next(gen)
# next(gen)
# gen.send(100)
# gen.throw(ValueError("Invalio Value"))
# # gen.close()
# next(gen)


# 使い道
# import sys
# list_a = [i for i in range(1000000)]
# def num(max):
#     i += 0
#     while i < max:
#         yield i
#         i += 1
#
# gen = num(1000000)
# print(sys.getsizeof(list_a))
# print(sys.getsizeof(gen))


#サブジェネレ-タ
def sub_sub_genertor():
    yield "SubSubのyield"
    return "sub sub のreturn"

def sub_genertor():
    yield "subのジェネレータ"
    res = yield from sub_sub_genertor()
    print("sub res = {}".format(res))
    return "subのreturn"

def genertor():
    yield "genertorのyield"
    res = yield from sub_genertor()
    print("genrtor={}".format(res))
    return "genertorのreturn"

gen = genertor()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

