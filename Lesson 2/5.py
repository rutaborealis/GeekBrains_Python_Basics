# Lesson 2
# Task 5
rating = [7, 5, 3, 3, 2]

while True:
    user_answer = input('Do you want to enter any new item in rating? Answer yes / no: ').lower()
    if user_answer == 'yes':
        new_item = input('Enter the number: ')
        if new_item.isdigit():
            num = int(new_item)
            rating.append(num)
            rating.sort(reverse=True)
        else:
            print('Please enter a natural number!')
        print(rating)
    if user_answer == 'no':
        break
