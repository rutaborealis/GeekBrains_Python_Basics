# Lesson 5
# Task 1
import os.path


def write_in_file(mode, text):
    """Write text in a file.

        To stop: ''
        """
    with open('Text_1.txt', mode) as file_lesson_1:
        while text != '':
            file_lesson_1.write(text + '\n')
            text = input('Enter text: ')
        print('Program completed')


text = input('Enter text: ')
file_exist = os.path.exists('Text_1.txt')  # True/False

if file_exist:
    write_in_file('a', text)
else:
    write_in_file('x', text)
