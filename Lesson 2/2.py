# Lesson 2
# Task 2
# new empty list
result_list = []

# fill the list
while True:
    user_answer = input('Do you want to add any elements in list? Answer yes / no: ').lower()
    if user_answer == 'yes':
        i = input('Enter the element of list: ')
        result_list.append(i)
    if user_answer == 'no':
        break

print(f'Original list: {result_list}')

# rearrangement of elements
if len(result_list) % 2 == 0:
    for i in range(0, len(result_list), 2):
        result_list[i], result_list[i + 1] = result_list[i + 1], result_list[i]
else:
    for i in range(0, len(result_list) - 1, 2):
        result_list[i], result_list[i + 1] = result_list[i + 1], result_list[i]

print(f'List with reversed elements {result_list}')
