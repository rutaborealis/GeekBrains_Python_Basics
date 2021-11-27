# Lesson 5
# Task 5
from random import randint
from functools import reduce

numbers = [str(randint(0, 100)) for i in range(50)]

with open('Text_5.txt', 'w') as file_lesson_5:
    file_lesson_5.write(' '.join(numbers))

with open('Text_5.txt', 'r') as file_lesson_5:
    content = file_lesson_5.read()

result = reduce(lambda x, y: int(x)+int(y), content.split())

print('Entered numbers:', *numbers, '\n'
      f'Sum of numbers: {result}')