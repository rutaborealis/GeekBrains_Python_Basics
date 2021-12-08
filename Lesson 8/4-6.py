# Lesson 8
# Task 4 - 6
import os.path
import json
import random
from abc import ABC, abstractmethod


class Storage():
    def __init__(self, storage={}):
        self.storage = storage

    def add_item(self, item):
        self.storage.update({item.id: (item.name, item.price, item.type)})
        print(f'Successfully added!')

    def delete_item(self, id_delete):
        del storage.storage[id_delete]
        print(f'Successfully deleted!')

    def get_items(self):
        for key, item in self.storage.items():
            print(f'id: {key}\n'
                  f'name: {item[0]}\n'
                  f'price: {item[1]}\n'
                  f'type: {item[2]}\n')

    def save_file(self):
        with open('Storage.json', 'w') as storage_json:
            json.dump(self.storage, storage_json)


class Item(ABC):
    def __init__(self, id=None, name=None, price=0.0):
        self.id = id
        self.name = name
        self.price = price


class Laptop(Item):
    def __init__(self, id=None, name=None, price=0.0, type='laptop'):
        self.id = id
        self.name = name
        self.price = price
        self.type = type


class MobilePhone(Item):
    def __init__(self, id=None, name=None, price=0.0, type='mobile phone'):
        self.id = id
        self.name = name
        self.price = price
        self.type = type


class Tablet(Item):
    def __init__(self, id=None, name=None, price=0.0, type='tablet'):
        self.id = id
        self.name = name
        self.price = price
        self.type = type


# storage = Storage({10: ('macbook', 125000.0, 'laptop'), 20: ('iphone x', 90000.0, 'mobile phone'), 30: ('ipad', 80000.0, 'tablet')})
# storage = Storage()
file_exist = os.path.exists('Storage.json')  # True/False
if file_exist:
    with open('Storage.json') as storage_json:
        storage = Storage(json.load(storage_json))
else:
    storage = Storage()

while True:
    quit = input('Enter "stop" to quit or "Enter": ')
    if quit != 'stop':
        print(f'Choose operation\n',
              '1. Add item in storage\n',
              '2. Delete item from storage\n',
              '3. Show all items in storage')
        operation = int(input('Enter the number of operation (1, 2, or 3): '))
        if operation == 1:
            item = input('Enter the type of item (Laptop, Mobile phone or Tablet only!): ').lower()
            if item == 'laptop':
                laptop = Laptop(id=random.randint(1, 100), name=input('Enter the name of laptop: '),
                                price=float(input('Enter the price of laptop: ')))
                storage.add_item(laptop)
            elif item == 'mobile phone':
                mobilephone = MobilePhone(id=random.randint(1, 100), name=input('Enter the name of mobile phone: '),
                                          price=float(input('Enter the price of mobile phone: ')))
                storage.add_item(mobilephone)
            elif item == 'tablet':
                tablet = Tablet(id=random.randint(1, 100), name=input('Enter the name of tablet: '),
                                price=float(input('Enter the price of tablet: ')))
                storage.add_item(tablet)
            else:
                print(f'\033[31mPlease enter the correct type of item!\033[30m')
        elif operation == 2:
            print(f'All items in storage: ')
            storage.get_items()
            id_delete = int(input(f'Enter ID of item to delete: '))
            try:
                storage.delete_item(id_delete)
            except:
                print(f'\033[31mUncorrect ID!\033[30m')
                continue
        elif operation == 3:
            print(f'All items in storage: ')
            storage.get_items()
        else:
            print(f'\033[31mPlease enter the correct number of operation!\033[30m')
    else:
        storage.save_file()
        print('Program completed')
        break
