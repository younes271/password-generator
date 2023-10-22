import string
import random

def password_generator(length=8):
    all = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all) for i in range(length))
    return password

print(password_generator(10))
