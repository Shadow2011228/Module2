import json

with open('Cities.json', 'r') as file: # Открывает и читает из файла .json
    python_dict = json.load(file)

for i in python_dict:
    print(i)

