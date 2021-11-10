# Lesson 1
# Task 4
n_original = int(input('Enter the number: '))
maximum = n_original % 10
n = n_original

while n > 0:
    digit = n % 10
    if digit > maximum:
        maximum = digit
    n = n // 10

print(f'Max digit in number {n_original}: {maximum}')
