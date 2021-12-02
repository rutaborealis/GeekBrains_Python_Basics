# Lesson 6
# Task 3
class Worker:
    def __init__(self, name=None, surname=None, position=None, wage=0.0, bonus=0.0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": float(wage), "bonus": float(bonus)}  # protected attribute


class Position(Worker):
    def __init__(self, name=None, surname=None, position=None, wage=0.0, bonus=0.0):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_total_income(self):
        income = self._income['wage'] + self._income['bonus']
        return income


worker = Position('Ruta', 'Borealis', 'junior data-scientist', 40000, 10000)
print(f'Position: {worker.position}')
print(f'Employee full name: {worker.get_full_name()}')
print(f'Employee total income: {worker.get_total_income()}')
