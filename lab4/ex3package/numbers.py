def is_even(num):
    return num % 2 == 0

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)