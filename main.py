import random
passlen = int(input("enter the length of password"))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@3#$%^&*()?/"
p = "".join(random.sample(s, passlen))
print(p)