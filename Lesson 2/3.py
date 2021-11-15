# Lesson 2
# Task 3
# dictionary realization
months_dict = {1: 'Winter', 2: 'Winter', 3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer',
               8: 'Summer', 9: 'Autumn', 10: 'Autumn', 11: 'Autumn', 12: 'Winter'}

while True:
    user_answer = input('Do you want to enter month number? Answer yes / no: ').lower()
    if user_answer == 'yes':
        user_month = int(input('Enter the month number: '))
        if 1 <= user_month <= 12:
            season = months_dict.get(user_month)
            print(f'It\'s {season}')
        else:
            print('Enter the month number 1 - 12!')
    if user_answer == 'no':
        break

# list realization
months_list = ['Winter', 'Winter', ' Spring', 'Spring', 'Spring', 'Summer', 'Summer', 'Summer', 'Autumn', 'Autumn',
               'Autumn', 'Winter']

while True:
    user_answer = input('Do you want to enter month number? Answer yes / no: ').lower()
    if user_answer == 'yes':
        user_month = int(input('Enter the month number: '))
        if 1 <= user_month <= 12:
            season = months_list[user_month - 1]
            print(f'It\'s {season}')
        else:
            print('Enter the month number 1 - 12!')
    if user_answer == 'no':
        break
