# Lesson 6
# Task 2
class Road:
    def __init__(self, length, width):
        self._length = length  # protected attribute
        self._width = width  # protected attribute

    def mass_of_asphalt(self, mass, thickness):
        mass_of_asphalt_tons = self._length * self._width * mass * thickness
        mass_of_asphalt_kg = mass_of_asphalt_tons / 1000
        return mass_of_asphalt_kg


road = Road(float(input('Enter the lenght of the road: ')), float(input('Enter the width of the road: ')))
mass = float(input('Mass of asphalt for covering one square meter of the road with asphalt: '))
thickness = float(input('Asphalt thickness: '))
print(f'Mass of asphalt: {road.mass_of_asphalt(mass, thickness)} tons')
