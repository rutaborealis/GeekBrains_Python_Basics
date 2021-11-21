# Lesson 3
# Task 4
# 1 realization
def my_func(x, y):
    return f'Exponentiation {x} and {y} result: {x ** y}'


a = float(input('Enter a positive real number: '))
b = int(input('Enter a negative integer: '))
print(my_func(a, b))


# 2 realization
def my_func(x, y):
    y = -y
    result = 1
    for i in range(1, y + 1):
        result = result * (1 / x)
    return result


a = float(input('Enter a positive real number: '))
b = int(input('Enter a negative integer: '))
print(my_func(a, b))
