# Lesson 3
# Task 6
def capitalization(array):
    output_array = []
    for i in array:
        output_array.append(str(i).capitalize())
    return ' '.join(output_array)


text_list = input('Enter a text separated by a space: ').split(' ')
print(capitalization(text_list))
