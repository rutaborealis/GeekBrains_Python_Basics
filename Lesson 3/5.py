# Lesson 3
# Task 5
def sum_numbers_1(array):
    index_end = array.index('q')
    slice = array[:index_end]
    sum = 0
    for i in slice:
        sum = sum + int(i)
    return sum


def sum_numbers_2(array):
    sum = 0
    for i in array:
        sum = sum + int(i)
    return sum


total = 0
while True:
    numbers = input('Enter a string of numbers separated by a space: ').lower()
    numbers = numbers.strip()
    numbers = numbers.split(' ')
    if 'q' in numbers:
        total = total + sum_numbers_1(numbers)
        print(f'Sum of entered numbers: {total}')
        break
    else:
        total = total + sum_numbers_2(numbers)
        print(f'Sum of entered numbers: {total}')
