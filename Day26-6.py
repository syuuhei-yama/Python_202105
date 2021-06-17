#グローバル変数

# def print_animal():
#     global animal
#     animal = "Cat"
#     print("関数内のanimal = {}, id = {}".format(animal, id(animal)))
#
# # animal = "Dog"
# print_animal()
# print("関数外のamimal = {}, id = {}".format(animal, id(animal)))

#インナー関数
def outer():
    outer_value = "外側の処理"
    def inner():
        nonlocal outer_value
        outer_value = "内側の変数"
        print("inner:outer_value = {}, id = {}".format(outer_value, id(outer_value)))
    inner()
    print("outer:outer_value={}, id = {}".format(outer_value, id(outer_value)))

outer()