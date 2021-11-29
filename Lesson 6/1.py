# Lesson 6
# Task 1
import turtle
from time import sleep

COLORS = ['red', 'yellow', 'green']


class TrafficLight:
    __color = None  # private attribute

    def __init__(self):
        self.__color = 'red'
        self.counter = 6

    def running(self):
        i = COLORS.index(self.__color)
        counter = 0
        while counter < self.counter:
            if i == 0:
                # self.__color = COLORS[i]
                # print(f'\033[31m\033[41m{self.__color}')
                turtle.color(COLORS[i])
                turtle.begin_fill()
                turtle.circle(50)
                turtle.end_fill()
                i = 1
                sleep(7)
            elif i == 1:
                # self.__color = COLORS[i]
                # print(f'\033[33m\033[43m{self.__color}')
                turtle.color(COLORS[i])
                turtle.sety(-100)
                turtle.begin_fill()
                turtle.circle(50)
                turtle.end_fill()
                i = 2
                sleep(2)
            elif i == 2:
                # self.__color = COLORS[i]
                # print(f'\033[32m\033[42m{self.__color}')
                turtle.color(COLORS[i])
                turtle.sety(-200)
                turtle.begin_fill()
                turtle.circle(50)
                turtle.end_fill()
                i = 0
                sleep(7)
                turtle.clearscreen()
                turtle.resetscreen()
            counter += 1


light = TrafficLight()
light.running()
