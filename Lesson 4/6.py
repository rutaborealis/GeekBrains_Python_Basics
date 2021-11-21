# Lesson 4
# Task 6
from itertools import count
from itertools import cycle

# 1 script
n, step = int(input('Enter the natural number: ')), int(input('Enter the natural number for step: '))

for i in count(n, step):
    if i > 100:
        break
    else:
        print(i)

# 2 script
text = '*'

i = 0
for item in cycle(text):
    if i > 10:
        break
    else:
        print(item * i)
    i = i + 1