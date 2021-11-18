# Lesson 3
# Task 1
def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = 'Zero division error! Divisor cannot be zero!'
    return result


x, y = float(input('Enter dividend: ')), float(input('Enter divisor: '))

print(division(x, y))
