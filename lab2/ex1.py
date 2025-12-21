name = input('Введите имя: ')
def greet(name):
    return f'Привет, {name}!'
print(greet(name))

number = int(input('Введите число: '))
def square(num):
    return num * num
print(square(number))

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return 'Числа равны!'
print(max_of_two(num1, num2))