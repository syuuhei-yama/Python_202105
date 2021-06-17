# y = [1, 2, 3, 4, 5]
# x = 1
# if x in y:
#     print("in")
# a = 1
# b = 2
# if not a != b:
#     print("Not")
# is_ok = True
# if  is_ok:
#     print("hello")


# is_ok = []
# if is_ok:
#     print("Ok")
# else:
#     print("No")


# is_empty = None
# # print(help(is_empty))
# if is_empty is None:   #isはNoneを判定するために用いる
#     print("None")
# a = None
# print(a is None)


# count = 0
# while count < 5:
#     print(count)
#     count += 1
# count = 0
# while True:
#     if count >= 5:
#         break
#     if count == 2:
#         count += 1
#         continue
#     print(count)
#     count += 1


# count = 0
# while count < 5:
#     if count == 1:
#         break
#     print(count)
#     count += 1
# else:
#     print("done")


# while True:
#     word = input("Enter:")
#     if word == "ok":
#         break
#     print("Next")


# some_list = [1, 2, 3, 4, 5]
# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1
# for i in some_list:
#     print(i)
# for s in "abcde":
#     print(s)
# for word in ["My","name","is","yama"]:
#     print(word)


# for fruit in ["apple","banana","orange"]:
#     if fruit == "banana":
#         break
#     print(fruit)
# else:
#     print("I ate all!")


# num_list =[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in num_list:
#     print(i)
# for _ in range(10):
#     print("hello")


for i, fruit in enumerate(["apple","banana","orange"]):
    print(i, fruit)
