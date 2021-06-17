#文字列
# fruit = "apple"
# print(fruit * 10)
# new_fruit = fruit + " banana"
# print(new_fruit)

#count
# msg = "ABCDEABC"
# print(msg.count("ABC"))

#startswith, endwith
# print(msg.startswith("ABCD"))
# print(msg.endswith("DC"))

#strip(両橋) rstrip lstrip
# msg = ' ABC '
# print(msg)
# print(msg.strip())
# msg = "ABCDEFABC"
# print(msg.strip("CBA"))
# print(msg.rstrip("CBA"))
# print(msg.lstrip("CBA"))


#upper, lower, swapcase, replace, capitaliza
msg = "abcABC"
msg_u = msg.upper()
msg_l = msg.lower()
msg_s = msg.swapcase()
print(msg_u,msg_l,msg_s)

msg = "ABCDEABC"
msg_r = msg.replace("ABC","FFF",-1)
print(msg_r)

msg = "hello world"
print(msg.capitalize())