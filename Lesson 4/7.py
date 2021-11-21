# Lesson 4
# Task 7
def fact(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
        yield result


n = 1
for i in fact(int(input('Enter the natural number: '))):
    print(f'{n}! = {i}')
    n = n + 1
