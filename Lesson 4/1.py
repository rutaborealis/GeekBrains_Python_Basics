# Lesson 4
# Task 1
import sys

arguments = sys.argv[1:]


def payroll(hours, rate, bonus):
    """Returns the payroll calculation.

    Formula: (hours * rate) + bonus
    Parameteters:
    hours
    rate
    bonus

    """
    result = ((hours * rate) + bonus)
    return result


print('Hours:', float(arguments[0]), 'Rate:', float(arguments[1]), 'Bonus:', float(arguments[2]), 'Result:',
      payroll(float(arguments[0]), float(arguments[1]), float(arguments[2])))
