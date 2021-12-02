# Lesson 6
# Task 4
class Car:
    def __init__(self, speed=None, color=None, name=None, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'The car {self.name} is going!')
        self.show_speed()

    def stop(self):
        print(f'The car {self.name} stopped')
        self.speed = 0
        self.show_speed()

    def turn(self, direction):
        print(f'The car {self.name} turned {direction}.')
        self.show_speed()

    def show_speed(self):
        print(f'Current speed of {self.name}: {self.speed}')


class TownCar(Car):
    def __init__(self, speed=None, color=None, name=None, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        print(f'Current speed is {self.speed}')
        if float(self.speed) > 60:
            print(f'\033[31m60 - is a max speed for town cars!!!\033[30m')
        else:
            print('\033[32mSpeed is OK!\033[30m')


class SportCar(Car):
    def __init__(self, speed=None, color=None, name=None, is_police=False):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed=None, color=None, name=None, is_police=False):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        print(f'Current speed is {self.speed}')
        if float(self.speed) > 40:
            print('\033[31m60 - is a max speed for work cars!!!\033[30m')
        else:
            print('\033[32mSpeed is OK!\033[30m')


class PoliceCar(Car):
    def __init__(self, speed=None, color=None, name=None, is_police=False):
        super().__init__(speed, color, name, is_police=True)

    def police(self):
        if self.is_police == True:
            print(f'{self.name} - is Police car!')


cadillac_xt4 = Car(100, 'blue', 'Cadillac XT4', False)
cadillac_xt4.go()
cadillac_xt4.turn('left')
cadillac_xt4.stop()
print()

cadillac_xt5 = TownCar(110, 'white', 'Cadillac XT5', False)
cadillac_xt5.go()
cadillac_xt5.turn('right')
cadillac_xt5.stop()
print()

cadillac_xt6 = SportCar(120, 'red', 'Cadillac XT6', False)
cadillac_xt6.go()
cadillac_xt6.turn('left')
cadillac_xt6.stop()
print()

cadillac_escalade = WorkCar(35, 'black', 'Cadillac Escalade', False)
cadillac_escalade.go()
cadillac_escalade.turn('right')
cadillac_escalade.stop()
print()

chevrolet_tahoe = PoliceCar(60, 'blue', 'Chevrolet Tahoe', True)
chevrolet_tahoe.police()
chevrolet_tahoe.go()
chevrolet_tahoe.turn('left')
chevrolet_tahoe.stop()
