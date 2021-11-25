# Lesson 5
# Task 3
with open('Text_3.txt', 'r') as file_lesson_3:
    content = file_lesson_3.readlines()

dict_employees = {}
i = 0
for item in content:
    item_list = item.split()
    dict_employees[i] = (item_list[0], float(item_list[1]))
    i = i + 1

sum_salary = 0
print(f'Employees with a salary less than 20000.00: ')
for item in dict_employees:
    sum_salary = sum_salary + dict_employees[item][1]
    if dict_employees[item][1] <= 20000:
        print(f'{dict_employees[item][0]} - {dict_employees[item][1]:.2f}')

print()

average_salary = sum_salary / len(dict_employees)
print(f'Total employees - {len(dict_employees)}\n'
      f'Average salary: {average_salary:.2f}')
