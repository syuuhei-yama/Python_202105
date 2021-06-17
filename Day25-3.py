#練習問題

#1
num = 10

#2
print(type(num))

#3
num_s = str(num)
print(type(num_s))

#4
num_list = [num_s, '20','30']
print(num_list)

#5
num_list.append('40')
print(num_list)

#6
num_tuple = tuple(num_list)
print(type(num_tuple))

#7
val = input()
num_tuple += (val,)
print(num_tuple)

#8
num_set = {"40","50","60"}
# print(type(num_set))

print("num_tuple={}".format(num_tuple))
print("num_set={}".format(num_set))

#9
print(set(num_tuple).union(num_set))

#10
num_dict = {
    num_tuple: num_s
}

#11
print(len(num_list))

#12
print(num_dict.get("Mykey","Does Not exitst"))

#13
num_list.extend(["50","60"])
print("num_list={}".format(num_list))

#14
val = input()
is_under_50 = int(val) < 50
print("is_under_50={}".format(is_under_50))

#15
print(f'num_s = {num_s}')

#16
print(dir(num_dict))


