def register(username, password):
    with open('users.txt', 'a') as file:
        file.write(f'{username}:{password}\n')

# Функция для проверки существования пользователя
def user_exists(username):
    with open('users.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, _ = line.strip().split(':')
            if stored_username == username:
                return True
        return False
    
def check_password(username, password):
    with open('users.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            stored_username, stored_password = line.strip().split(':')
            if stored_username == username and stored_password == password:
                return True
        return False