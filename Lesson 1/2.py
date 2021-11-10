# Lesson 1
# Task 2
n = int(input('Enter time in seconds: '))

hours = n // 3600
minutes = (n - (hours * 3600)) // 60
seconds = n - (hours * 3600) - (minutes * 60)

print(f'Time in format hh:mm:ss: {hours:02}:{minutes:02}:{seconds:02}')
