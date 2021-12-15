# Lesson 8
# Task 3
class ListValidationError(Exception):

    def __init__(self, text):
        self.text = text

    @staticmethod
    def validation(text):
        try:
            return float(text)
        except:
            print(f'\033[31mThe item must be a number!\033[30m')
            return None


result_list = []

while True:
    quit = input('Enter "stop" to quit or "Enter": ')
    if quit != 'stop':
        result = ListValidationError.validation(input('Enter a number: '))
        if result != None:
            result_list.append(result)
        else:
            continue
    else:
        print(result_list)
        print('Program completed')
        break
