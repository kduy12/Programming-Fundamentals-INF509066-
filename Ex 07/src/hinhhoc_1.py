import math


# Tạo một module tên là hinhhoc_1.py chứa các hàm tính chu vi, diện tích của
# hình chữ nhật, hình tam giác, hình tròn.

def rectangle_perimeter(width, length):
    return 2 * (width + length)


def rectangle_area(width, length):
    return width * length


def triangle_perimeter(a, b, c):
    return a + b + c


def triangle_area(a, b, c):
    p = triangle_perimeter(a, b, c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))


def circle_circumference(r):
    return 2 * math.pi * r


def circle_area(r):
    return math.pi * r * r
