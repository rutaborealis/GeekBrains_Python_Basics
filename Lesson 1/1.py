# Lesson 1
# Task 1
name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = int(input('Enter your age: '))

if age >= 18:
    print(f'Hello, {name} {surname}!')
    print(f'Your age is {age}.')
    print(f'Access is allowed!')
else:
    print(f'Hello, {name} {surname}!')
    print(f'Your age is {age}.')
    print(f'Sorry. Access is denied.')
