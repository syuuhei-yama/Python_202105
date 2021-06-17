#ループ処理
# for i in range(10):
#     print(i)

# for _ in range(100):
#     print("A")

# for i in range(2, 20, 3):
#     print(i)

# sample = ["jhon","paul","George","Ringo"]
# sample = ("jhon","paul","George","Ringo")
# for member in sample:
#     print(member)

# human = {
#     "Name":"syuuhei",
#     "Age":"24",
#     "gender":"Man"
# }
# for h in human:
#     print(h, human.get(h))


# 2
# fruit = ["Grep","Pine","Apple"]
# for key, value in enumerate(fruit):
#     print("index={}".format(key))
#     print("value={}".format(value))

# classA = ["Taro","Hanako","Jiro"]
# classB = ["katuo","Wakame","Taro"]
# for A,B in zip(classA,classB):
#     print("classA={}".format(A))
#     print("classB={}".format(B))
#
# count = 0
# while count < 10:
#     print(count)
#     count += 1


# 3
for i in range(10):
    if i == 3:
        continue
        # break
    print(i)
else:
    print("処理終了")

num = 0
while num < 10:
    if num == 5:
        num += 1
        continue
    # if num == 7:
    #     break
    print(num)
    num += 1
else:
    print("whileループ終了")


