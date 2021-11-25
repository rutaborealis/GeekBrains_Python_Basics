# Lesson 5
# Task 4
from deep_translator import GoogleTranslator

with open('Text_4.txt', 'r') as file_lesson_4:
    content = file_lesson_4.readlines()

result = GoogleTranslator(target='ru').translate_batch(content)

with open('Text_4_translated.txt', 'w') as file_lesson_4_translated:
    for item in result:
        print(item, file=file_lesson_4_translated)



