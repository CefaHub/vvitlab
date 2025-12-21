name = input('Введите имя: ')
age = input('Введите возраст: ')

def describe_person(name, age):
    if age == '':
        return f'{name}, 30'
    else:
        return f'{name}, {age}'
result = describe_person(name, age)
print(result)