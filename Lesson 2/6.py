# Lesson 2
# Task 6
def search_by_key(key):
    output_dict = {}
    output_list = []
    for item in goods:
        name_item = item[1].get(key)
        output_list.append(name_item)
        output_dict[f'{key}'] = output_list
    return output_dict


goods = []
item_dict = {}
j = 1

# fill the 'Goods'
while True:
    user_answer = input('Do you want to enter any new items in \'Goods\'? Answer yes / no: ').lower()
    if user_answer == 'yes':
        n = int(input('How many items do you want to enter? Your answer: '))
        for i in range(n):
            item_dict = {}
            name = input('Enter the name of item: ').lower()
            item_dict['name'] = name
            cost = float(input('Enter the cost of item: '))
            item_dict['cost'] = cost
            amount = int(input('Enter the amount: '))
            item_dict['amount'] = amount
            units = input('Enter units: ').lower()
            item_dict['units'] = units
            goods.append((j, item_dict))
            j = j + 1
        print(f'Entered positions:\n{goods}\n\n')
    if user_answer == 'no':
        break
print(f'Total positions in \'Goods\':\n{goods}\n\n')

# goods = [(1, {'name': 'macbook', 'cost': 200000.00, 'amount': 15, 'units': 'un'}),
#          (2, {'name': 'iphone', 'cost': 150000.00, 'amount': 20, 'units': 'un'}),
#          (3, {'name': 'ipad', 'cost': 80000.00, 'amount': 15, 'units': 'un'}),
#          (4, {'name': 'apple pencil', 'cost': 10000.00, 'amount': 10, 'units': 'un'})]
# print(f'{goods} \n \n')

# searching by key in 'Goods'
while True:
    user_answer = input('Do you want to search any items in \'Goods\'? Answer yes / no: ').lower()
    if user_answer == 'yes':
        key = input('Enter key for search in \'Goods\': ').lower()
        output_dict = search_by_key(key)
        print(f'Result for entered key - {key}:\n{output_dict}\n\n')
    if user_answer == 'no':
        break
