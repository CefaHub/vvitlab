from lab4 import my_module

number_a = float(input("Введите первое число:"))
number_b = float(input("Введите второе число:"))

def result_sum(number_a, number_b):
    return my_module.sum(number_a, number_b)
print('Результат:', result_sum(number_a, number_b))
