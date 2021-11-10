# Lesson 1
# Task 6
a = float(input('Result in 1st day: '))
b = float(input('Planning result: '))

increase = 0.1
day = 1
n = a
print(f'{day} day planning result: {n:0.2f}')

while n < b:
    n = n + (n * increase)
    day = day + 1
    print(f'{day} day planning result: {n:0.2f}')

print(f'On the {day} day the athlete achieved a result of at least {n:0.2f} km.')
