# Lesson 5
# Task 7
import json

with open('Text_7.txt', 'r') as file_lesson_7:
    content = file_lesson_7.readlines()

print('Companies performance data: ')
result_dictionary = {}
total_result = 0
count = 0
for item in content:
    item_list = item.split()
    company = item_list[0]
    result = float(item_list[2]) - float(item_list[3])
    if result >= 0:
        total_result = total_result + result
        count = count + 1
    print(f'Company: {company}; Result: {result:.2f}')
    result_dictionary[item_list[0]] = float(item_list[2]) - float(item_list[3])

average_profit = total_result / count
print(f'Average profit: {average_profit:.2f}')

result_dictionary = [result_dictionary, {'average_profit': average_profit}]

with open('Text_7_json.json', 'w') as file_lesson_7_json:
    json.dump(result_dictionary, file_lesson_7_json)
