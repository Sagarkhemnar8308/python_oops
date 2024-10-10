import random
import string

pass_len = 12
password = ""
val = string.ascii_letters + string.digits + string.punctuation

for i in range(pass_len):
    password = random.choice(val)
    print(password, end="")
