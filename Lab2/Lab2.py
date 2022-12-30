import json
from random import randint, choice
from pprint import pprint


def write(data, filename):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2)


def read(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)


class Person:
    def __init__(self):
        self.name
        self.id

data = {
    'Person': []
}

for i in range(50):
    data['Person'].append(Person().__dict__)

n_data = read('lab2.json')
print(n_data['Person'][49])
g = Person()

g.name = n_data['Person'][4]['name']

print(g.name)

input()
