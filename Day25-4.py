#制御文 if 1
# class ClassA:
#     def __init__(self,a):
#         self.a = a
#
#     def __bool__(self):
#         if self.a == "a":
#             return True
#         return False
#
#
# bool_var = ClassA("a")
# print(bool(bool_var))
#
# if bool_var:
#     print("if文の中の処理")

#if 2
# msg = "黄色"
# if msg == "blue":
#     print("進め")
# elif msg == "red":
#     print("止まれ")
# else:
#     print("それ以外")

# age = 60
# if age < 20:
#     print("20未満")
# elif age <= 40:
#     print("20以上、40以下です")
# elif age >= 60:
#     print("60以上です")
# else:
#     print("それ以外")
#
# #and or not
# gender = "woman"
# age = 30
# if gender == "man" or age < 20:
#     print("未成年もしくは男性です")
#
# if  gender != "man":
#     print("男ではない")


#all, any
if all((True, 10 < 20, "a" == "a")):
    print("allの中の処理")

if any((10 < 20, 10 < 5, "a" == "b")):
    print("anyの中の処理")

    