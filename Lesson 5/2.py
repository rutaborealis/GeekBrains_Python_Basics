# Lesson 5
# Task 2
with open('Text_2.txt', 'r') as file_lesson_2:
    content = file_lesson_2.readlines()

string_amount = len(content)
print(f'Number of string in file: {string_amount}')

i = 1
for item in content:
    words = item.split()
    words_amount = len(words)
    print(f'In {i} string there are: {words_amount} words')
    i = i + 1
