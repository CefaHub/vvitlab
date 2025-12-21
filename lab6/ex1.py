class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self.__password = new_password

    def check_password(self, password):
        return self.__password == password


print("Регистрация")
username = input("Введите имя: ")
email = input("Введите email: ")
password = input("Введите пароль: ")

user = UserAccount(username, email, password)

print("\nАккаунт успешно создан!\n")

while True:
    print("Что сделать?")
    print("1 — Сменить пароль")
    print("2 — Проверить пароль")
    print("3 — Выход")

    choice = input("Выбор: ")

    if choice == "1":
        new_pass = input("Введите новый пароль: ")
        user.set_password(new_pass)
        print("Пароль изменён")

    elif choice == "2":
        check = input("Введите пароль для проверки: ")
        if user.check_password(check):
            print("Пароль верный")
        else:
            print("Пароль неверный")

    elif choice == "3":
        print("Выход из программы")
        break

    else:
        print("Неизвестная команда")