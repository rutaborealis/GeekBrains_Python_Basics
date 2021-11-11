# Lesson 1
# Task 5
revenue = float(input('Enter revenue: '))
costs = float(input('Enter costs: '))
result = revenue - costs

if revenue > costs:
    print(f'The profit is: {result:0.2f}')
    print(f'Calculation of profitability (profit / revenue) = {(result / revenue * 100):0.2f}%')
    employees = int(input('Enter the number of employees: '))
    print(f'Profit per employee (profit / employees) = {(result / employees):0.2f}')
elif revenue < costs:
    print(f'The loss is: {result:0.2f}')
elif revenue == costs:
    print(f'The profit is 0.00')
