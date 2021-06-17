#セット
# set_a = {"a","b","c","d","a",12}
# print(set_a)
# print("e" in set_a)
# print("a" in set_a)
# print(len(set_a))
#
# #メソッド
# set_a.add("A")
# print(set_a)
#
# set_a.remove("a")
# print(set_a)
#
# set_a.discard(13)
# print(set_a)
#
# val = set_a.pop()
# print(val, set_a)
#
# set_a.clear()
# print(set_a)

#セット2
s = {"a","b","c","d"}
t = {"c", "d","e","f"}
u = s.union(t)
print(u)

u = s & t
print(u)

u = s - t
print(u)

u = s ^ t
print(u)

s |= t
print(s)


s = {"apple","banana"}
t = {"apple","banana","lemon"}
u = {"chery"}
print(s.issubset(t))
print(t.issuperset(s))
print(t.isdisjoint(s))
print(t.isdisjoint(u))