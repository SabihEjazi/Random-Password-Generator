import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBER = "0123456789"
Symbol = "{}[]#()&%^"

all=lower + upper + NUMBER + Symbol
length = 15
password = "".join(random.sample(all,length))
print("The password you generated is :",password)