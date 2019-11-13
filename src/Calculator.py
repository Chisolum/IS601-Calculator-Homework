import math
from decimal import Decimal
def addition(a,b):
    a = int(a)
    b =  int(b)
    c = a + b
    return c

def subtraction(a,b):
    a = int(a)
    b = int(b)
    c =  b - a
    return c

def multiplication(a,b):
    a = int(a)
    b =  int(b)
    c =  a*b
    return c

def division(a,b):
    a = int(a)
    b = int(b)
    c =  b/ a
    return round(c,9)


def square(a):
    a = int(a)
    c =   a * a
    return c

def sqrt(a):
    a = int(a)
    c =  a**.5
    if c > 10:
        c = round(c, 8)
    else:
        c = round(c, 9)
    return c


class Calculator:
        result = 0
        def __init__(self):
             pass
        def add(self,a,b):
            self.result = addition(a,b)
            return self.result
        def subtract(self,a,b):
            self.result = subtraction(a,b)
            return self.result
        def multiply(self,a,b):
            self.result = multiplication(a,b)
            return self.result
        def divide(self,a,b):
            self.result = division(a,b)
            return self.result
        def square(self,a):
            self.result = square(a)
            return self.result
        def sqrt(self,a):
            self.result = sqrt(a)
            return self.result