# Lesson 4
# Task 4
list_orginal = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

list_1 = [i for i in list_orginal if list_orginal.count(i) == 1]
print(list_1)