# Lesson 6
# Task 5
class Stationery:
    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print(f'Start rendering - {self.title}')


class Pen(Stationery):
    def __init__(self, title='pen'):
        super().__init__(title)

    def draw(self):
        print(f'Start rendering - {self.title}')


class Pencil(Stationery):
    def __init__(self, title='pencil'):
        super().__init__(title)

    def draw(self):
        print(f'Start rendering - {self.title}')


class Handle(Stationery):
    def __init__(self, title='handle'):
        super().__init__(title)

    def draw(self):
        print(f'Start rendering - {self.title}')


stick = Pen('stick')
stick.draw()

pen = Pen('blue pen')
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle('red handle')
handle.draw()