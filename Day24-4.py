#辞書
# car = {"brand":"Toyota","model":"plius","year":"2015",1:100}
# print(car["model"])
# print(car.get("bran", 12))
# print(car.get(1))
# print(car.keys())
# print(car.values())
# print(car.items())

# for k, v in car.items():
#     print("key={}, value={}".format(k, v))
#
# if "brand" in car:
#     print("Carのブランドは{}".format(car["brand"]))

#メソッド
# car = {"brand":"Toyota","model":"plius","year":"2015"}
# tmp_car = {"country":"japan","prefectuer":"Aichi","model":"カローラ"}
# car.update(tmp_car)
# print(car)

# car["city"] = "Toyota-si"
# car["year"] = 2021
# print(car)
#
# value = car.popitem()
# print(car)
# print(value)

# value = car.pop("model")
# print(car)
# print(value)
# car.clear()
# print(car)


#タプル
fruit = ("apple","banana","lemon")
print(fruit)
print(type(fruit))
print(fruit[0])

fruit = fruit + ("gerp",)
print(fruit)

list_fruit = ["apple","banana"]
fruit = tuple(list_fruit)
print(fruit)
print(fruit.count("apple"))
print(fruit.index("banana"))

pos = (135, 35)
countrys = {pos:"japan"}
print(countrys.get((135,35)))