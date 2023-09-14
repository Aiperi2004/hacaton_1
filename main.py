# main.py
from users import register, user_exists, check_password

# Функция для регистрации пользователя
def user_registration():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    if user_exists(username):
        print("Пользователь с таким именем уже существует.")
    else:
        register(username, password)
        print("Регистрация успешно завершена.")

# Функция для входа пользователя
def user_login():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    if check_password(username, password):
        print("Вход успешно выполнен.")
    else:
        print("Неправильное имя пользователя или пароль.")

if __name__ == "__main__":
    while True:
        print("1. Регистрация")
        print("2. Вход")
        print("3. Выход")
        choice = input("Выберите действие: ")

        if choice == "1":
            user_registration()
        elif choice == "2":
            user_login()
        elif choice == "3":
            break
        else:
            print("Некорректный выбор.")

