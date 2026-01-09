import  s_taper
from s_taper.consts import *
import random


scheme = {
    'user_id': INT + KEY,
    'name': TEXT,
    'age': FLT,
    'first': BLN,
}

users = s_taper.Taper('users', 'data.db').create_table(scheme)

scheme2= {
    "user_id": INT+KEY,
    'name': TEXT,
    "order_id": INT,
    "n": INT,
    "art": INT,
    "sum": INT
}

orders = s_taper.Taper('orders', 'data.db').create_table(scheme2)


# for i in range(3000):
#     c = random.randint(0,1)
#     age=random.randint(14,99)
#     names=['Alex', "Mark", "Daniel", "Rembo", "Jon", "Harry"]
#     b=random.choice(names)
#     user2_list=[i, b, age, c]
#     users.write(user2_list)

a=0
for i in users.read_all():
    user_list = i
    if i[2] > 71:
        print(i)
        a += 1
print(a)
b=a/3000
print(b)