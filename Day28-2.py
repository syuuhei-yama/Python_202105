#リスト内包表記
list_a = (1, 2, 3, "a", 4, "b")
new_list = [x*2 for x in list_a if type(x) == int]
print(new_list)
list_c = [x for x in range(100) if x % 7 == 0]
print(list_c)

dict_a = {
    'a':'Apple',
    'b':'Banana'
}
list_c = [dict_a.get(x) for x in list_a if type(x) == str]
print(list_c)
list_a = (x for x in range(100))
print(list_a)
def func(n):
    for x in range(2, n):
        if n % x == 0:
            return True
        return False

list_a = [func(x) for x in range(100) if func(x) == False]
print(list_a)