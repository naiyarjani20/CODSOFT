import random
import string
all=string.ascii_uppercase+string.digits+string.punctuation
length=int(input("Enter length of the password"))
print(length)
password = "".join(random.sample(all,length))
print("password is",password)
