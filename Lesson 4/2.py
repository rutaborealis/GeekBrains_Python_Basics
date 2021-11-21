# Lesson 4
# Task 2
list_orginal = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

list_1 = [list_orginal[i] for i in range(1, len(list_orginal)) if list_orginal[i] > list_orginal[i - 1]]
print(list_1)
