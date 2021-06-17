#データ構造の復習

# i = [1, 2, 3, 4, 5]
# j = i
# j[0] = 100
# print("j=",j)
# print('i=',i)

# x = [1, 2, 3, 4, 5]
# # y = x.copy()
# y = x[:]
# y[0] = 100
# print('x=',x)
# print('y=',y)



# t = ([1, 2, 3],[4, 5, 6])
# t[0][0] = 100
# print(t)
#
# s = 1, 2, 3
# print(type(s))

num_tuple = (30, 40)
print(num_tuple)

x, y = num_tuple
print(x, y)

min, max = 1, 1000
print(min, max)

a = 10
b = 100
a, b = b, a
print(a,b)