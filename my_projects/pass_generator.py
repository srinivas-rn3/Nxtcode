import random 
passlen = int(input("Enter tha password length:"))
chars = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = "".join(random.sample(chars, passlen))
print(p)
