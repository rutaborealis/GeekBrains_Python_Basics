# Lesson 2
# Task 1
result_list = [15, 42.5, 'Shipping better than perfection', True, False, None, (10, 20, 30), {'key_1': 'value_1'}]

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphabet_list = list(alphabet)

result_list.append(alphabet_list)

print(result_list)

for i in result_list:
    print(type(i))
