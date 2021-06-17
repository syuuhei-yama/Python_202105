# days = ["Mon", "Tue", "Wed"]
# fruits = ["apple", "banana", "orange"]
# drinks = ["coffee", "tea", "beer"]
#
# # for i in range(len(day)):
# #     print(day[i], fruit[i], drink[i])
#
# for day, fruit, drink in zip(days, fruits, drinks):
#     print(day, fruit, drink)


# d = {'x':100, 'y': 200}
# for k, v in d.items():
#     print(k,':', v)


# def say_something():
#     s = 'Hi'
#     return s
# reslut = say_something()
# print(reslut)

# def what_is_this(color):
#     if color == 'red':
#         return 'tomato'
#     elif color == 'green':
#         return 'kyabetu'
#     else:
#         return 'I dont NO'
# reslut = what_is_this('green')
# print(reslut)


# num: int = 10
# def add_num(a: int,  b: int) -> int:
#     return a + b
#
# r = add_num('a', 'b')
# print(r)


# def menu(entry='beef', drink='wine', dessart='ice'):
#     print('entry=',entry)
#     print('drink=',drink)
#     print('dessart=',dessart)
#
# menu(entry='chicken', drink='beer',)
# # menu(entry='beef',drink='beer',dessart='ice')


def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l
# y = [1, 2, 3]
# r = test_func(100, y)
# print(r)
# y = [1, 2, 3]
# r = test_func(200, y)
# print(r)
r = test_func(100)
print(r)

r = test_func(100)
print(r)