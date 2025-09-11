import math
def perimeter(a, b, c):
    return a + b + c


def area(a, b, c):
    p = perimeter(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))