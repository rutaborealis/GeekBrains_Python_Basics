# Lesson 8
# Task 7
class ComplexNumber():
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber((self.real * other.real - self.imaginary * other.imaginary),
                             (self.real * other.imaginary + other.real * self.imaginary))

    def __str__(self):
        if self.imaginary > 0:
            return f'{self.real}+{ self.imaginary}i'
        else:
            return f'{self.real}{self.imaginary}i'

num1 = ComplexNumber(2, 1)
num2 = ComplexNumber(3, -5)
print(num1 + num2)

num3 = ComplexNumber(3, 1)
num4 = ComplexNumber(2, -3)
print(num3 * num4)