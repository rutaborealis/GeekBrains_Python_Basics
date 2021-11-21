# Lesson 4
# Task 3
# list generation
list_orginal = [i for i in range(20, 241) if (i % 20 == 0) or (i % 21 == 0)]

# output
for i in list_orginal:
    if i % 20 == 0:
        print(f'{i} / 20 = {i / 20}')
    elif i % 21 == 0:
        print(f'{i} / 21 = {i / 21}')
