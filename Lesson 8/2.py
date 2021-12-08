# Lesson 8
# Task 2
class ZeroDivision(Exception):

    def __init__(self, dividend, devider):
        self.dividend = dividend
        self.devider = devider

    @staticmethod
    def devision_by_zero(dividend, devider):
        try:
            return (dividend / devider)
        except:
            return (f'\033[31mZero division error! Divisor cannot be zero!\033[30m')


while True:
    quit = input('Enter "end" to quit or "Enter": ')
    if quit != 'end':
        print(ZeroDivision.devision_by_zero(float(input('Enter dividend: ')), float(input('Enter dividend: '))))
    else:
        print('Program completed')
        break
