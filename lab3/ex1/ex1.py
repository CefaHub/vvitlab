def read_file(mode):
    with open('example.txt', 'r', encoding='utf-8') as file:
        if mode == 'all':
            print(file.read())
        elif mode == 'lines':
            for line in file:
                print(line.strip())

print('Чтение всего файла:')
read_file('all')
print('Построчное чтение:')
read_file('lines')
