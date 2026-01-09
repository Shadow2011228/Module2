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

user1_list = [101, 'Oleg', 29, 0] # Создаем список с записью в таблицу (кол-во элементов = столбцов)
users.write(user1_list) # используем метод write передавая 1 аргумент список, который хотим положить в таблицу

orders1_list=[34, "Кроссовки", 21, 2, 5309, 1500]
orders.write(orders1_list)


# for i in range(3000):
#     c = random.randint(0,1)
#     age=random.randint(14,99)
#     names=['Alex', "Mark", "Daniel", "Rembo", "Jon", "Harry"]
#     b=random.choice(names)
#     user2_list=[i, b, age, c]
#     users.write(user2_list)

scheme2 = {
    "user_id": INT,
    'name': TEXT,
}

users.create_table(scheme2, 'new')

new1_list = [101, 'skrillex-bangaram']
users.write(new1_list, 'new')

user_list = users.read('user_id', 0)
print(user_list)

users_list = users.read_all()
print(users_list)

users.delete_row('user_id', 0)

# users.drop_table()
# users.drop_table('a_999')

# users.delete_row('first', 1)

# user_list = users.read('user_id', random.randint(0,3000))
# print(user_list)
#
# for i in user_list:
#     print(i)

# for i in range(3000):
#     name='озон карта'
#     o=random.randint(1,3000)
#     n=random.randint(1,3000)
#     a=random.randint(1000,3000)
#     s=1
#     user3_list=[i, name, o, n, a, s]
#     orders.write(user3_list)


# scheme3 = {
#     "user_id": INT,
#     'name': TEXT,
# }
# for i in range(3000):
#     users.create_table(scheme3, f'a_{i}')

# for i in range(1000, 3000):
#     users.drop_table(f'a_{i}')

user_list = users.read('age', 70)
print(user_list)