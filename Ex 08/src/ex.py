# ▸Write a Python program:
# 1.to handle a ZeroDivisionError exception when dividing a number by zero.
def division(a, b):
    try:
        return a/b
    except ZeroDivisionError as zde:
        print('You cannot divide a number with zero:', zde)
# 2.that prompts the user to input an integer and raises a ValueError exception
# if the input is not a valid integer.
def input_integer():
    try:
        return int(input("Enter an integer:"))
    except ValueError as ve:
        print('You must enter an integer:', ve)

# 3.that prompts the user to input two numbers and raises a TypeError
# exception if the inputs are not numerical.
def input_2_numbers():
    a = input('Enter the first number:')
    b = input('Enter the second number:')
    try:
        a_num = float(a)
        b_num = float(b)
        return a_num, b_num
    except Exception:
        raise TypeError('Inputs must be numerical values')

# 4.that executes an operation on a list and handles an IndexError exception
# if the index is out of range.

def access_element(my_list, index):
    try:
        return my_list[index]
    except IndexError:
        print('Index is out of range')

# 5.that prompts the user to input a number and handles a KeyboardInterrupt
# exception if the user cancels the input.
def input_until_break():
    try:
        while True:
            a = input('Enter a number: ')
    except KeyboardInterrupt:
        print("\nEnd!")
# 6.that executes division and handles an ArithmeticError exception
# if there is an arithmetic error.
def _division(a, b):
    try:
        return a / b;
    except ArithmeticError as ae:
        print('Arithmetic error:', ae)


if __name__ == '__main__':
    _division(1, 0)
