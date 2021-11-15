# Lesson 2
# Task 4
# 1 realization
while True:
    user_answer = input('Do you want to enter any text? Answer yes / no: ').lower()
    if user_answer == 'yes':
        user_text = input('Enter any text: ')
        text_list = user_text.split(' ')
        for i in range(len(text_list)):
            word = text_list[i]
            if len(word) < 10:
                print(f'{i + 1} - {word}')
            else:
                print(f'{i + 1} - {word[0:10]}')
    if user_answer == 'no':
        break

# 2 realization enumerate()
while True:
    user_answer = input('Do you want to enter any text? Answer yes / no: ').lower()
    if user_answer == 'yes':
        user_text = input('Enter any text: ')
        text_list = user_text.split(' ')
        for i, element in enumerate(text_list, 1):
            if len(element) < 10:
                print(f'{i} - {element}')
            else:
                print(f'{i} - {element[0:10]}')
    if user_answer == 'no':
        break
