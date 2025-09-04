# 1.Write a Python function to find the maximum of three numbers.
def max_of_3(a: float, b: float, c: float) -> float:
    res = a
    if b > a and b > c:
        res = b
    if c > b and c > a:
        res = c
    return res


# 2.Write a Python function to sum all the numbers in a list.
def sum_list(lst: list) -> float:
    res = 0.0
    for i in lst:
        res += i
    return res


# 3.Write a Python program to reverse a string.
def reverse_string(s: str) -> str:
    return s[::-1]


# 4.Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.
def factorial(n: int) -> int:
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


# 5.Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n: int) -> bool:
    from math import isqrt
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


# 6.Write a Python function to print
#   1.all prime numbers that less than a number (enter prompt keyboard).
def primes_left_than_n(n: int):
    for i in range(n + 1):
        if is_prime(i):
            print(i, end=' ')


#   2.the first N prime numbers
def first_n_primes(n: int):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            print(num, end=' ')
            count += 1
        num += 1


# 7.Write a Python function to check whether a number is "Perfect" or not.
# Then print all perfect number that less than 1000.
# A perfect number is a positive integer that is equal to the sum of its
# proper divisors (divisors excluding itself).

def is_perfect(n: int) -> bool:
    from math import isqrt
    if n < 2:
        return False
    sum_divisor = 1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            sum_divisor += i
            if i != n // i:  # neu i la uoc cua n thi n/i cung la uoc cua n
                sum_divisor += n  # kiem tra i co khac n/i khong de tranh cong trung 1 uoc
    return sum_divisor == n


# 8.Write a Python function to check whether a string is a pangram or not.
def is_pangram(s: str) -> bool:
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(s)


if __name__ == '__main__':

