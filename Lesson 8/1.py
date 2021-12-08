# Lesson 8
# Task 1
import datetime
import re

now = datetime.datetime.now()


class Date:
    def __init__(self, date):
        self.date = Date.validation(date)

    @classmethod
    def to_int(cls, date):
        date_list = re.findall("\d+", date)
        result = [int(i) for i in date_list]
        return result

    @staticmethod
    def validation(date):
        date_list = Date.to_int(date)
        if date_list[0] < 1 or date_list[0] > 31:
            print('The day must be between 1 and 31! By default, we set it to today.')
            date_list[0] = int(now.day)
        if date_list[1] < 1 or date_list[1] > 12:
            print('The month must be between 1 and 31! By default, we set it to today.')
            date_list[1] = int(now.month)
        if date_list[2] < 1900 or date_list[2] > 2035:
            print('The year must be between 1900 and 2035! By default, we set it to today.')
            date_list[2] = int(now.year)
        return date_list


# date = Date('01 12 2021')
# date = Date('02/12/2021')
# date = Date('03-12-2021')
# date = Date('32-13-2036')
date = Date('00-00-1889')
print('Date: ' + '.'.join([str(i) for i in date.date]))
