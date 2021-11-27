# Lesson 5
# Task 6
import re
from functools import reduce

with open('Text_6.txt', 'r') as file_lesson_6:
    content = file_lesson_6.readlines()

dictionary_subjects = {}
index = 0
for item in content:
    hours_list = re.findall("\d+", item)
    dictionary_subjects[index] = (item[:item.find(':')], int(reduce(lambda x, y: int(x) + int(y), hours_list)))
    index = index + 1

print(dictionary_subjects)
