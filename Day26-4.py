#例外処理
# try:
#     b = [10, 20, 30]
#     c = b.method_a()
#     a = b[4]
#     a = 10 / 0
# except ZeroDivisionError as e:
#     import traceback
#     traceback.print_exc()
#     # print(e, type(e))
#     pass
# except IndexError as e:
#     print("エラー発生")
# except Exception as e:
#     print("全てのエラー",e, type(e))
# else:
#     # a = 10 / 0
#     print("elseの処理")
# finally:
#     print("Finally処理")
#
#
# print("処理が完了しました")


#raise 例外自作
class MyException(Exception):
    pass

def devide(a, b):
    if b == 0:
        raise MyException("0では割り切れない")
    else:
        return a / b

try:
    c = devide(10, 0)
except Exception as e:
    print(e, type(e))




