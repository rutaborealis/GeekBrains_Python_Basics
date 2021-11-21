# Lesson 3
# Task 3
def my_func(x, y, z):
    list = []
    for i in (x, y, z):
        list.append(i)
    maximum_1 = max(list)
    list.remove(maximum_1)
    maximum_2 = max(list)
    return f'You entered 3 numbers: {x}, {y}, {z}.\nSum of {maximum_1} + {maximum_2} = {maximum_1 + maximum_2}'


a, b, c = float(input('Enter a: ')), float(input('Enter b: ')), float(input('Enter c: '))
print(my_func(a, b, c))
