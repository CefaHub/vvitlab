text = input('Введите текст: ')
with open('user_input.txt', 'w', encoding='utf-8') as file:
    file.write(text)
print('Текст записан в файл user_input.txt')

add_text = input('Введите текст для добавления в файл: ')
with open('user_input.txt', 'a', encoding='utf-8') as file:
    file.write('\n' + add_text)
print('Текст добавлен в файл user_input.txt')
